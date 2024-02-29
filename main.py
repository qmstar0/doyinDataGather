import webview


def create_window():
    # 创建一个窗口，指定 URL 或本地 HTML 文件
    webview.create_window("My Web App", "https://baidu.com")


if __name__ == '__main__':
    # 在主线程中运行创建窗口的函数
    create_window()
    # 运行主循环，启动应用程序
    webview.start()
