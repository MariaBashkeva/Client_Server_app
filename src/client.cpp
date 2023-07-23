
#include <windows.h>
#include <wininet.h>
#include <iostream>
#include <string>

#pragma comment(lib, "wininet.lib")

const std::string SERVER_URL = "http://127.0.0.1:5000/api";

int main() {
    while (true) {
        HINTERNET hInternet = InternetOpenA("MyApp", INTERNET_OPEN_TYPE_DIRECT, NULL, NULL, 0);
        if (hInternet) {
            HINTERNET hConnection = InternetConnectA(hInternet, SERVER_URL.c_str(), INTERNET_DEFAULT_HTTP_PORT, NULL, NULL, INTERNET_SERVICE_HTTP, 0, 1);
            if (hConnection) {
                HINTERNET hRequest = HttpOpenRequestA(hConnection, "POST", "/endpoint", NULL, NULL, NULL, INTERNET_FLAG_RELOAD, 1);
                if (hRequest) {
                    const char* data = "work_activity_data_here";
                    HttpSendRequestA(hRequest, NULL, 0, (LPVOID)data, strlen(data));
                    InternetCloseHandle(hRequest);
                }
                InternetCloseHandle(hConnection);
            }
            InternetCloseHandle(hInternet);
        }
        Sleep(5000);
    }

    return 0;
}
