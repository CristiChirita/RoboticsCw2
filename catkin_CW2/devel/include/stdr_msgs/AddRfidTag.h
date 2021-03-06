// Generated by gencpp from file stdr_msgs/AddRfidTag.msg
// DO NOT EDIT!


#ifndef STDR_MSGS_MESSAGE_ADDRFIDTAG_H
#define STDR_MSGS_MESSAGE_ADDRFIDTAG_H

#include <ros/service_traits.h>


#include <stdr_msgs/AddRfidTagRequest.h>
#include <stdr_msgs/AddRfidTagResponse.h>


namespace stdr_msgs
{

struct AddRfidTag
{

typedef AddRfidTagRequest Request;
typedef AddRfidTagResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct AddRfidTag
} // namespace stdr_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::stdr_msgs::AddRfidTag > {
  static const char* value()
  {
    return "257a3ebd6cd76d8346fa749295629845";
  }

  static const char* value(const ::stdr_msgs::AddRfidTag&) { return value(); }
};

template<>
struct DataType< ::stdr_msgs::AddRfidTag > {
  static const char* value()
  {
    return "stdr_msgs/AddRfidTag";
  }

  static const char* value(const ::stdr_msgs::AddRfidTag&) { return value(); }
};


// service_traits::MD5Sum< ::stdr_msgs::AddRfidTagRequest> should match 
// service_traits::MD5Sum< ::stdr_msgs::AddRfidTag > 
template<>
struct MD5Sum< ::stdr_msgs::AddRfidTagRequest>
{
  static const char* value()
  {
    return MD5Sum< ::stdr_msgs::AddRfidTag >::value();
  }
  static const char* value(const ::stdr_msgs::AddRfidTagRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::stdr_msgs::AddRfidTagRequest> should match 
// service_traits::DataType< ::stdr_msgs::AddRfidTag > 
template<>
struct DataType< ::stdr_msgs::AddRfidTagRequest>
{
  static const char* value()
  {
    return DataType< ::stdr_msgs::AddRfidTag >::value();
  }
  static const char* value(const ::stdr_msgs::AddRfidTagRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::stdr_msgs::AddRfidTagResponse> should match 
// service_traits::MD5Sum< ::stdr_msgs::AddRfidTag > 
template<>
struct MD5Sum< ::stdr_msgs::AddRfidTagResponse>
{
  static const char* value()
  {
    return MD5Sum< ::stdr_msgs::AddRfidTag >::value();
  }
  static const char* value(const ::stdr_msgs::AddRfidTagResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::stdr_msgs::AddRfidTagResponse> should match 
// service_traits::DataType< ::stdr_msgs::AddRfidTag > 
template<>
struct DataType< ::stdr_msgs::AddRfidTagResponse>
{
  static const char* value()
  {
    return DataType< ::stdr_msgs::AddRfidTag >::value();
  }
  static const char* value(const ::stdr_msgs::AddRfidTagResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // STDR_MSGS_MESSAGE_ADDRFIDTAG_H
