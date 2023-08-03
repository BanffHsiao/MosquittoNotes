## Start 
You can make changes to the configuration by editing:
  ```
  /opt/homebrew/etc/mosquitto/mosquitto.conf
  ```

To start mosquitto now and restart at login:
  ```
  brew services start mosquitto
  ```
Or, if you don't want/need a background service you can just run:
  ```
  /opt/homebrew/opt/mosquitto/sbin/mosquitto -c /opt/homebrew/etc/mosquitto/mosquitto.conf
  ```
  
 ## Elements in Mosquitto
 1. Publisher : send messages
 2. Broker : send the recieved messages to subscriber
 3. subscriber : recieve messages from Broker

 ## Mosquitto test
 build up a subscriber, set title to "A"
 (host is set to localhost in default)
 ```
 mosquitto_sub -t A
 ```
 open another terminal, and build up a publisher. The title is also set to "A". After that, send message "Message" to the subscriber.
 ```
 mosquitto_pub -t A -m Message
 ```
 To set subscriber id to 00001, type
 ```
 mosquitto_sub -i 00001 -t A
 ```

 ## First try: modify Mosquitto.conf
 1. set persistence to true
 ```
 persistence true
 ```
 2. set the name of db file
 ```
 persistence_file mosquitto.db
 ```
 3. set the path of the db file
 ```
 persistence_location /opt/homebrew/etc/mosquitto
 ```
 4. set the autosave interval to 1 second
 ```
 autosave_interval 1
 ```
 5. To read file mosquitto.db, type
 ```
 git clone https://github.com/eclipse/mosquitto
 cd mosquitto/apps/db_dump
 make
 sudo ./mosquitto_db_dump /var/lib/mosquitto/mosquitto.db
 ```
 6. output
 ```
 Mosquitto DB dump
 CRC: 0
 DB version: 6
 DB_CHUNK_CFG:
	Length: 16
	Shutdown: 0
	DB ID size: 8
	Last DB ID: 7873
 ```
 
 ## Second try: modify log file
 1. set destination log file
 ```
 log_dest file /opt/homebrew/etc/mosquitto/mosquitto.log
 ```
 2. set the type of log
 ```
 log_type subscribe
 ```
 3. client connection messages included
 ```
 connection_messages true
 ```
 4. use local5
 ```
 log_facility 5
 ```
 5. add timestamp value to the log
 ```
 log_timestamp true
 ```
 6. make timestamp readable
 ```
 log_timestamp_format %Y-%m-%dT%H:%M:%S
 ```
 7. result:
     (1) subscribe
     ```
     2023-08-02T17:42:45: Received SUBSCRIBE from 00001
     2023-08-02T17:42:45: 	A (QoS 0)
     2023-08-02T17:42:45: 00001 0 A
     2023-08-02T17:42:45: Sending SUBACK to 00001
     2023-08-02T17:42:45: Received SUBSCRIBE from 00002
     2023-08-02T17:42:45: 	A (QoS 0)
     2023-08-02T17:42:45: 00002 0 A
     2023-08-02T17:42:45: Sending SUBACK to 00002
     ```
     (2) publish to subscribers
     ```
     2023-08-02T17:42:53: Sending PUBLISH to 00001 (d0, q0,      r0, m0, 'A', ... (2 bytes))
     2023-08-02T17:42:53: Sending PUBLISH to 00002 (d0, q0,      r0, m0, 'A', ... (2 bytes))
     ```
     (3) disconnect
     ```
     2023-08-02T17:54:12: Received DISCONNECT from 00001
     2023-08-02T17:54:12: Client 00001 disconnected.
     2023-08-02T17:54:13: Received DISCONNECT from 00002
     2023-08-02T17:54:13: Client 00002 disconnected.
     ```