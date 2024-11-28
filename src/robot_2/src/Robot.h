#ifndef ROBOT_H
#define ROBOT_H

#include <string>
#include <vector>
#include <deque>
#include <unordered_map>
#include <memory>
#include <thread>
#include <mutex>

#include <geometry_msgs/Pose.h>
#include <move_base_msgs/MoveBaseAction.h>
#include <actionlib/client/simple_action_client.h>

#include "WarehouseObject.h"
#include "Storage.h"
#include "Product.h"
#include "Order.h"
#include "Dispatch.h"
#include "OrderController.h"

// Robot operational status types
enum RobotStatus
{
    offline,
    startup,
    standby,
    requestOrder,
    processOrder,
    plan,
    moveToStorage,
    requestProduct,
    moveToDispatch,
    dispatchOrder,
    closeOrder,
};

// Autonomous Mobile Robot class
class Robot : public WarehouseObject
{
public:
    Robot(std::string robotName,
          std::string actionName,
          std::vector<std::shared_ptr<Storage>> &Bstorages,
          std::vector<std::shared_ptr<Storage>> &Rstorages,
          std::vector<std::shared_ptr<Dispatch>> &dispatches,
          std::shared_ptr<OrderController> orderController);
    ~Robot();
    void SetStatus(RobotStatus status);
    RobotStatus GetStatus();
    std::vector<std::string> GetCargoBinProductsName();
    void StartOperation();

private:
    std::string _actionName{};                               // SimpleActionClient name
    std::vector<std::shared_ptr<Storage>> _Bstorages;         // Vector of available BStorage
    std::vector<std::shared_ptr<Storage>> _Rstorages;         // Vector of available RStorage
    std::vector<std::shared_ptr<Dispatch>> _dispatches;      // Vector of available Dispatch
    std::shared_ptr<OrderController> _orderController;       // OrderController
    RobotStatus _status{RobotStatus::offline};               // Current RobotStatus
    std::shared_ptr<Order> _order;                           // Current Order
    std::mutex _cargoBinMtx;                                 // Mutex to access and modify _cargoBinProducts
    std::vector<std::unique_ptr<Product>> _cargoBinProducts; // Products stored in the robot cargo bin

    std::deque<std::shared_ptr<Storage>> GetStoragesToGo();
    bool Move(actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> &ac, geometry_msgs::Pose goal);
    bool Move_arm(actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> &ac, geometry_msgs::Pose goal);
    void Operate();
};

#endif