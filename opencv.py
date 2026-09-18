import cv2
def to_grayscale(image_path, output_path="gray_output.jpg"):
    # 读取图像
    img = cv2.imread(image_path)
    if img is None:
        return False, "图片读取失败，请检查路径"
    # 转灰度
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 保存
    cv2.imwrite(output_path, gray)
    # 展示图片
    cv2.imshow("Gray Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return True, f"成功，灰度图保存至 {output_path}"


if __name__ == "__main__":
    # 桌面图片路径
    res, msg = to_grayscale(r"C:\Users\33879\Desktop\1.png")
    print(msg)
