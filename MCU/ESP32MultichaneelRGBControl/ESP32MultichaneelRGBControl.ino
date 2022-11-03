#include <WiFi.h>  //wifi功能需要的库 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>必须在MPU之后
WiFiUDP Udp;//声明UDP对象
#include <FastLED.h>
#define LED_PIN     5
#define NUM_LEDS    6
CRGB leds[NUM_LEDS];
const char* wifi_SSID="NewDrWiki-1";  //存储AP的名称信息
const char* wifi_Password="88860879";  //存储AP的密码信息
uint16_t udp_port=1122;  //存储需要监听的端口号
char incomingPacket[9];  //存储Udp客户端发过来的数据
char To_IP[] = "192.168.3.8";
int Port = 8090;

union myCo{
  uint8_t s[9];
};
  
myCo myc;


[[noreturn]] void Task_Send(void *parameter){
  int num = 0;
  Udp.beginPacket(To_IP, Port);  //准备发送数据到目标IP和目标端口
  Udp.println(WiFi.localIP());
  Udp.endPacket();  //向目标IP目标端口发送数据
  delay(500);
  Udp.beginPacket(To_IP, Port);  //准备发送数据到目标IP和目标端口
  Udp.println(WiFi.localIP());
  Udp.endPacket();  //向目标IP目标端口发送数据
  delay(500);
  Udp.beginPacket(To_IP, Port);  //准备发送数据到目标IP和目标端口
  Udp.println(WiFi.localIP());
  Udp.endPacket();  //向目标IP目标端口发送数据
  delay(500);
    while(1){
        vTaskDelay(1);
    }
    vTaskDelete(NULL);
}

[[noreturn]] void Task_Receive(void *parameter){
    while(1){
        if(Udp.parsePacket()>0){//如果有数据那么Data_length不为0，无数据Data_length为0
            int len = Udp.read(incomingPacket, 9);  //读取数据，将数据保存在数组incomingPacket中
            if (len > 0){  //为了避免获取的数据后面乱码做的判断
                Serial.println(incomingPacket);
                // Red
                for (int i = 0; i <= 1; i++) {
                  leds[i] = CRGB ( incomingPacket[0], incomingPacket[1],incomingPacket[2]);
                  FastLED.show();
                  delay(1);
                }
              
                // Green
                for (int i = 2; i <= 3; i++) {
                  leds[i] = CRGB ( incomingPacket[3], incomingPacket[4],incomingPacket[5]);
                  FastLED.show();
                  delay(1);
                }
              
                //  Blue
                for (int i = 4; i <= 5; i++) {
                  leds[i] = CRGB ( incomingPacket[6], incomingPacket[7],incomingPacket[8]);
                  FastLED.show();
                  delay(1);
                }
            }
        }
        vTaskDelay(10);
    }
    vTaskDelete(NULL);
}

void setup() {
  Serial.begin(115200);
      WiFi.begin(wifi_SSID, wifi_Password);
    while (WiFi.status() != WL_CONNECTED){
        delay(1000);
        Serial.println("...");
    }
    Serial.print("WiFi connected with IP: ");
    Serial.println(WiFi.localIP());
    Udp.begin(udp_port);//启动UDP监听这个端口
    Serial.println(xPortGetCoreID());
    xTaskCreate(Task_Send, "Task_Send", 10000, NULL, 1, NULL);
    xTaskCreate(Task_Receive, "Task_Receive", 10000, NULL, 1, NULL);
    delay(1000);
    FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
}

void loop(){
    delay(1000);
}
