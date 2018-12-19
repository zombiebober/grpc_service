package server

import (
	pb "GRPC/server/store"
	"bufio"
	"context"
	"fmt"
	"log"
	"math/rand"
	"net"
	"os"

	"google.golang.org/grpc"
)

const (
	port = ":4444"
)

type Server struct {
	discountDB map[uint32]pb.Discount
}

/*
type ProductKey struct {
	ID uint64
}

func (pr *pb.Discount) Key() ProductKey {
	return ProductKey{pr.Id}
}
*/

func (s *Server) GetDiscount(ctx context.Context, product *pb.Product) (*pb.Discount, error) {
	val, ok := s.discountDB[product.Id]
	if !ok {
		return &pb.Discount{Error: &pb.Error{State: true, Message: "Not found"}}, nil
	} else {
		return &pb.Discount{Error: &pb.Error{State: false}, Id: val.Id, Currency: val.Currency, Price: val.Price}, nil
	}
}

func main() {
	lis, err := net.Listen("tcp", port)
	defer lis.Close()
	if err != nil {
		log.Fatalf("Faled to listen %v", err)
	}
	server := Server{}
	server.discountDB = generate()
	grpcServer := grpc.NewServer()
	pb.RegisterDiscountServiceServer(grpcServer, &server)
	if err := grpcServer.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %s", err)
	}
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter ramdom text:")
	_, _ = reader.ReadString('\n')
}

func generate() map[uint32]pb.Discount {
	discount := make(map[uint32]pb.Discount)
	for i := 0; i < 50; i++ {
		discount[uint32(i)] = pb.Discount{
			Error:    &pb.Error{State: false},
			Id:       uint32(i),
			Currency: pb.Currency_RUB,
			Price:    float32(rand.Intn(100 * i)),
		}
	}
	return discount
}
