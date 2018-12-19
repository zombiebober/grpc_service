import grpc
import product_pb2
import product_pb2_grpc
import random
channel = grpc.insecure_channel('localhost:4444')

client = product_pb2_grpc.DiscountServiceStub(channel)

dataProduct = {1:product_pb2.Product(id=3,id_client="test",name="Product"
                               ,price=random.random()),
               101:product_pb2.Product(id=3,id_client="test",name="Product1"
                               ,price=random.random())}
print(dataProduct)
for key,elem in dataProduct:
    response = client.GetDiscount(elem)
    print(response)