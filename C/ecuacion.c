#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

void calcular_ecuacion(int min, int max, int opcion);
void saludo();
void menu();
int comprobar_numero(int *num, int min_valido);

int main(){
    int opcion;
    bool salida = false;
    int min = -100, max = 100;
    while (!salida)
    {
        menu(); 
        scanf("%d", &opcion);
        switch (opcion)
        {
        case 1:
        calcular_ecuacion(min, max, opcion);
        break;
        case 2:
        calcular_ecuacion(min, max, opcion);
        break;
        case 3:
        calcular_ecuacion(min, max, opcion);
        break;
        default:
        salida=true;
            break;
        }

    }
    
}

void calcular_ecuacion (int min, int max, int opcion) {
    int num1,num,num2,num3, num4;
    float respuesta,calculo,total;
    switch (opcion)
    {
    case 1:
        srand(time(0));
        num1 = rand() % (max - min + 1) + min;
        num2 = rand() % (max - min + 1) + min;
        num = rand() % (max - min + 1) + min;
        float calculo = num1 - (num2);
        float total = num / calculo;  
        if (calculo!=0)
        {
            printf("Indica el resultado de la ecuacion %dx = %dx + %d es x = ??", num1, num2, num);
            scanf("%f",&respuesta);
            if (respuesta==total){
                printf("\n\tCorrecta! La solucion es %.1f \n", respuesta);
                }
                else{
                    printf("\n\tIncorrecta! La solucion era %.1f \n", total);
                }
        }
            else{
            printf("Lo sentimos pero parece que esta ecuación no la podemos calcular, ya que  el denominador es cero.\n");
            printf("Error division por cero\n");
            
            }
        break;
    case 2:
        printf("introduce un numero distinto para a 0\n");
        comprobar_numero(&num, 1);
        srand(time(0));
        num = rand() % (max - min + 1) + min;
        num1 = rand() % (max - min + 1) + min;
        calculo = num / num1;

        printf("Indica el resultado de la ecuacion  %dx = %d ", num1, num);
            scanf("%f",&respuesta);
            if (respuesta==calculo){
                printf("\n\tCorrecta! La solucion es %.2f \n", respuesta);
                }
                else{
                    printf("\n\tIncorrecta! La solucion era %.2f \n", calculo);
                }
    break;
    default:

        printf("\nPor razones de control de errores tienes que introducir el valor de a y de b.");
        printf("\nIntroduce el valor de a.");
        scanf("%d",&num1);
        printf("\nIntroduce el valor de b.");
        scanf("%d",&num2);
        srand(time(0));
        
        num = rand() % (max - min + 1) + min;
        num1 = rand() % (max - min + 1) + min;
        num2 = rand() % (max - min + 1) + min;
        num3 = rand() % (max - min + 1) + min;
        num4 = rand() % (max - min + 1) + min;
        
        float calculo_a_b = num1 + num2;
        float calculo_c_d = num3 + num4;
        total = calculo_c_d / calculo_a_b;  
        if (calculo_a_b!=0)
        {
            printf("Indica el resultado de la ecuacion %dx %dx = %d + %d , x = ??", num1, num2, num3, num4, total);
            scanf("%f",&respuesta);
            if (respuesta==total){
                printf("\n\tCorrecta! La solucion es %.2f \n", respuesta);
                }
                else{
                    printf("\n\tIncorrecta! La solucion era %.2f \n", total);
                }
        }
            else{
            printf("Lo sentimos pero parece que esta ecuación no la podemos calcular, ya que  el denominador es cero.\n");
            printf("Error division por cero\n");
            
            }
    break;
    }



}

void saludo(){
    printf("\n----------------------------------------------------");
    printf("\nBienvenido usuario a la calculadora de ecuaciones.");
    printf("\n-----------------------------------------------------");
}


void menu(){
    printf("\n1. ax = bx +- c");
    printf("\n2. ax = b");
    printf("\n3. ax + bx = c + d");
    printf("\n4. Salir del programa.");
    printf("\nIntroduce una opcion :");
}


int comprobar_numero(int *num, int min_valido){
    printf("Introduce un dato\n");
    do{
        scanf("%d", num);
        if(*num == min_valido){
            printf("El valor %d debe de ser distinto de %d. Introduce uno nuevo: \n", *num, min_valido);
        }else{
            printf("DATO CORRECTAMENTE INTRODUCIDO\n");
        }
    }while(*num==min_valido);
}