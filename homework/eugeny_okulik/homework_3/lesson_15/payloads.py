


blog_body = {
    "category": "a32934c5-77c9-4617-b533-8d6fd85165c7",  # valid UUID
    "name": "Test Blog Post for Automation",  # safe blog title
    "description": (
        "This blog post is created solely for automation testing purposes. "
        "It contains multiple sentences to simulate a realistic blog post with meaningful content. "
        "The description explains the purpose of testing, including validation of API endpoints, "
        "ensuring correct data handling, and verifying that images and videos are processed properly. "
        "It also covers integration points, testing workflows, and expected system behavior under different scenarios. "
        "All content is neutral, safe, and non-repetitive to ensure it passes the API content filter. "
        "This helps QA engineers reliably test blog creation functionality without encountering errors. "
        "By using clear, informative, and structured content, this post simulates real-world usage while "
        "avoiding spam-like patterns or sensitive phrases. Automation scripts can depend on this text "
        "to consistently verify the blog creation endpoint in both development and staging environments."
    ),
    "main_image_url": "http://api.inexlynk.com/media/image/2025/11/19/pytest_b4c885b1f22e44d0.png",
    "images": [
        {"image_url": "http://api.inexlynk.com/media/image/2025/11/19/pytest_b4c885b1f22e44d0.png"},
        {"image_url": "http://api.inexlynk.com/media/image/2025/11/19/pytest_vs_unittest_a_detailed_comparison_9f30ac73df_bff0ca453a07481e.png"},
        {
            "image_url": "http://api.inexlynk.com/media/image/2025/11/19/pytest_b4c885b1f22e44d0.png"},
        {
            "image_url": "http://api.inexlynk.com/media/image/2025/11/19/pytest_vs_unittest_a_detailed_comparison_9f30ac73df_bff0ca453a07481e.png"}
    ],
    "videos": [
        {"video_url": "https://www.youtube.com/shorts/M5CqflezzsI"}
    ]
}

patch_blog_body = {
  "name": "Test Blog Post for Automation",
    "description": (
        "This blog post is created solely for automation testing purposes. "
        "It contains multiple sentences to simulate a realistic blog post with meaningful content. "
        "The description explains the purpose of testing, including validation of API endpoints, "
        "ensuring correct data handling, and verifying that images and videos are processed properly. "
        "It also covers integration points, testing workflows, and expected system behavior under different scenarios. "
        "All content is neutral, safe, and non-repetitive to ensure it passes the API content filter. "
        "This helps QA engineers reliably test blog creation functionality without encountering errors. "
        "By using clear, informative, and structured content, this post simulates real-world usage while "
        "avoiding spam-like patterns or sensitive phrases. Automation scripts can depend on this text "
        "to consistently verify the blog creation endpoint in both development and staging environments."
    ),
  "main_image_url": "http://api.inexlynk.com/media/image/2025/11/19/pytest_b4c885b1f22e44d0.png",
  "is_archive": False,
  "added_images": [
    {
      "image_url": "http://api.inexlynk.com/media/image/2025/11/19/pytest_b4c885b1f22e44d0.png"
    },
    {
      "image_url": "http://api.inexlynk.com/media/image/2025/11/19/pytest_b4c885b1f22e44d0.png"
    }
  ],
  "added_videos": [
    {
      "video_url": "http://api-inextlynk.upgrow.uz/media/files_and_images/Memati-sahnalari-qashqirlarmakoni-memati_jSyWZFa.mp4"
    }
  ],
  "removed_images": [],
  "removed_videos": []
}


DEVICE_INFO_ME = {
    "device_id": "e3980453-e09a-439a-b165-4d9e5518e4eb",
    "firebase_token": "",
    "platform": "android",
    "os_version": "string",
    "device_model": "string",
    "location": "Uzbekistan"
}

login_me = {
    "device": DEVICE_INFO_ME,
    "email": "nurimen738@gmail.com",
    "password": "1"
}



DEVICE_INFO_ANOTHER = {
    "device_id": "SKQ1.210908.001",
    "firebase_token": "",
    "platform": "android",
    "os_version": "12",
    "device_model": "Xiaomi M2101K7AI",
    "location": "Uzbekistan"
  }

login_another = {
    "device": DEVICE_INFO_ANOTHER,
    "email": "ignore@gmail.com",
    "password": "1"
}