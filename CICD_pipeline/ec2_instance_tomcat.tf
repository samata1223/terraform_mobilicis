terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

# Create an EC2 instance
resource "aws_instance" "example_instance" {
  ami           = "ami-0ff8a91507f77f867"
  instance_type = "t2.micro"
  key_name      = "my_key"
  subnet_id     = "my_subnet"
 user_data = <<-EOF
    #!/bin/bash
    apt-get update
    apt-get install -y default-jdk
    apt-get install -y tomcat8
    systemctl start tomcat8
  EOF
  tags = {
    Name = "my-instance"
  }
}
