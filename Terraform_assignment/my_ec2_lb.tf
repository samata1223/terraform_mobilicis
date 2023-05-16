
# Create EC2 instances
resource "aws_instance" "my_instance" {
  ami           = "ami-0ff8a91507f77f867"
  instance_type = "t2.micro"
  count = "2"
  subnet_id     = aws_subnet.example_subnet.id
  security_group_ids = [aws_security_group.my_sg.id]
}

# Create a listener for the load balancer
resource "aws_lb_listener" "example_listener" {
  load_balancer_arn = aws_lb.my_lb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.my_target_group.arn
  }
}
