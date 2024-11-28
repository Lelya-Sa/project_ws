#ifndef ORDERCONTROLLER_H
#define ORDERCONTROLLER_H

#include <vector>
#include <string>
#include <memory>
#include <thread>
#include <mutex>
#include <geometry_msgs/Pose.h>
#include <std_msgs/String.h>
#include <deque>
#include <condition_variable>
#include <list>
#include <unordered_map>
#include "WarehouseObject.h"
#include "Order.h"

class OrderController : public WarehouseObject
{
public:
    OrderController(std::string orderControllerName);
    ~OrderController();
    void AddOrder(const std_msgs::String &str);
    void CloseOrder(std::shared_ptr<Order> order);
    std::vector<std::shared_ptr<Order>> GetOrdersTracking();
    std::shared_ptr<Order> RequestNextOrder(std::string robotName);
    std::shared_ptr<Order> RequestNextOrderWithTimeout(std::string robotName, int timeoutMs);

private:
    // Double ended map that keep received Orders and their processing time
    std::unordered_map<std::shared_ptr<Order>, int > _map;
    std::unordered_map<std::shared_ptr<Order>, int > _Rgraph; // graph of distances
    std::condition_variable _mapCond;                  // Condition variable to handle Order requests
    std::mutex _mapMtx;                                // Map mutex
    std::mutex _ordersTrackingMtx;                       // Orders tracking mutex
    std::vector<std::shared_ptr<Order>> _ordersTracking; // Vector of Orders that are being executed by robots
};

#endif