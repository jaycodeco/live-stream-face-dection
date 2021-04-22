# Live Streaming and Face Detection with flask and opencv

### to Run development Server
```python
python app.py
```

### to use an external Ip Camera/CCTV/RTSP Link
```python
cv2.VideoCapture('rtsp://username:password@camera_ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp')
```
~

### to use laptop builtin webcam
- cv2.VideoCapture(0)
```python
cv2.VideoCapture(0)
```
