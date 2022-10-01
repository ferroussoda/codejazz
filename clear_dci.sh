#! /bin/bash
sudo docker rmi --force registry-ip:5000/frontend
sudo docker rmi --force frontend
sudo docker rmi --force registry-ip:5000/todos-api             
sudo docker rmi --force todos-api                            
sudo docker rmi --force log-message-processor                
sudo docker rmi --force registry-ip:5000/log-message-processor 
sudo docker rmi --force registry-ip:5000/auth-api              
