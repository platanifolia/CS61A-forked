#include <8052.h> // 引用头文件


#define ADDR0 P1_0
#define ADDR1 P1_1
#define ADDR2 P1_2
#define ADDR3 P1_3
#define ENLED P1_4


//========= 延时 ============
void delay_ms(unsigned int s){

    unsigned int x;

    for(s;s>0;s--){
        x = 98;
        while(x--);
    }
}

//================ 主函数 ===================

void main(){

    unsigned char i;
    
    ENLED = 0;
    ADDR3 = 1;
    ADDR2 = 1;
    ADDR1 = 1;
    ADDR0 = 0;

    while(1){ //主循环
    
        P0 = 0xff;

        delay_ms(150);

        for(i = 0;i<8;i++){
            P0 = P0 <<1;
            delay_ms(150);
        }

        P0 = 0xff;
        
        delay_ms(150);

        for(i = 0;i<8;i++){
            P0 = P0 >>1;
            delay_ms(150);
        }
    }
}