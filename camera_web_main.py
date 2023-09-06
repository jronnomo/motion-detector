import streamlit as st
import cv2
import datetime

st.title("Camera Web App")
capture_video = st.button("Start Camera")

if capture_video:
    image = st.image([])
    video = cv2.VideoCapture(1)

    while True:
        currentTime = datetime.datetime.now()
        day = currentTime.strftime("%A")
        time = currentTime.strftime("%d/%m/%Y %H:%M:%S")
        check, frame = video.read()
        video_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.putText(video_frame, day, (50, 50), cv2.FONT_HERSHEY_PLAIN,
                    2, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(video_frame, time, (50, 90), cv2.FONT_HERSHEY_PLAIN,
                    2, (0, 0, 255), 2, cv2.LINE_AA)

        image.image(video_frame)