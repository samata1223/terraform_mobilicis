1.Run terraform scripts in CICD Pipeline directory.
2."Jenkins_install_on_ec2_instance" will create ec2 instance and Jenkins will be isntalled on it
3. "ec2_instance_tomcat" will create ec2 instance and tomact will be installed on it.
4. Save Jenkinsfile in root directory of your application's repository. Commit and push the Jenkinsfile to your repository.
5. It will create a new pipeline job and configure it to use the Jenkinsfile from your repository. 
6. Make sure  Jenkins server has SSH access to the EC2 instance by configuring the necessary security groups and key pairs.


