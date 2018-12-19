# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import product_pb2 as product__pb2


class DiscountServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetDiscount = channel.unary_unary(
        '/store.DiscountService/GetDiscount',
        request_serializer=product__pb2.Product.SerializeToString,
        response_deserializer=product__pb2.Discount.FromString,
        )


class DiscountServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetDiscount(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DiscountServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetDiscount': grpc.unary_unary_rpc_method_handler(
          servicer.GetDiscount,
          request_deserializer=product__pb2.Product.FromString,
          response_serializer=product__pb2.Discount.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'store.DiscountService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
