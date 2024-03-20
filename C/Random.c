#include<stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include<time.h>
#include "Random.h"

//Esta es la funcion main.
int main(){
  int r1, r2, eleccion, min, max;
  char caracter;
  bool salida=false;
  printf("Introduce (s) si quieres elegir los máximos y los mínimos, sino , introduce (n).");
  scanf("%c", &caracter);
  if (caracter=='s' || caracter=='S'){
    preguntar_max_min( &max, &min);
    }
  else{
    max=10;
    min=1;
    }
  do
  {
    srand(time(0));
    r1 = rand() % (max - min + 1) + min;
    r2 = rand() % (max - min + 1) + min;

    menu();
    eleccion=comprobar_max_min(1, 5);
    switch (eleccion)
    {
    case 1:
      suma(r1, r2, salida);
    break;
    case 2:
      resta(r1, r2, salida);
    break;
    case 3:
      suma(r1, r2, salida);
    break;
    case 4:
    preguntar_max_min( &max, &min);
    break;
    default:
    salida=true;
      break;
    }
  } while (!salida);
  return 0;
}
/*
Esta funcion no recibe nada, ni devuelve nada, solo se encarga de mostrar por pantalla el menu de opciones
*/
void menu(){
  printf("\n======Calculadora======\n");
  printf("\t1. Suma\n");
  printf("\t2. Resta\n");
  printf("\t3. Multiplicación\n");
  printf("\t4. Cambiar máximos y mínimos\n");
  printf("\t5. Salir");
  printf("\nSeleccione una opción: ");
}

/*
Esta funcion recibe:dos punteros los cuales son nombrados como max y min.
El usuario modifica la información de max y min.
*/
void preguntar_max_min(int *max, int *min){
  printf("Ingrese el nuevo valor máximo para los números:\n");
  scanf("%d",max);
  printf("Ingrese el nuevo valor mínimo para los números:\n");
  scanf("%d",min);
}


void suma(int r1, int r2, bool salida){
  while (!salida)
  {
    int resultado;
    printf("%d + %d ", r1, r2);
    printf("\nIntroduce el resultado:");
    scanf("%d", &resultado);
    if (resultado == r1+r2 )
    {
      printf("\n***************************");
      printf("\n*¡Perfecto!, has acertado.*");  
      printf("\n***************************");
      salida=true;
    }
    else{
      char caracter;
      printf("\nLo siento, no has acertado.");
      
    }
  }
}



void resta(int r1, int r2, bool salida){
  while (!salida)
  {
    int resultado;
    printf("%d - %d ", r1, r2);
    printf("\nIntroduce el resultado:");
    scanf("%d", &resultado);
    if (resultado == r1-r2 )
    {
      printf("\n***************************");
      printf("\n*¡Perfecto!, has acertado.*");  
      printf("\n***************************");
      salida=true;
    }
    else{
      printf("\nLo siento, no has acertado.");
    }
  }
}

void multiplicacion(int r1, int r2, bool salida){
  while (!salida)
  {
    int resultado;
    printf("%d x %d ", r1, r2);
    printf("\nIntroduce el resultado:");
    scanf("%d", &resultado);
    if (resultado == r1*r2 )
    {
      printf("\n***************************");
      printf("\n*¡Perfecto!, has acertado.*");  
      printf("\n***************************");
      salida=true;
    }
    else{
      printf("\nLo siento, no has acertado.");
    }
  }
}

int comprobar_max_min(int min, int max){
  int n;
  bool salida=false;
  while (!salida)
  {
    scanf("%d", &n);
    if (n<min||n>max)
    {
      printf("\nLo sentimos pero el número que ha elegido está fuera del rango permitido, vuelve a intentarlo.\n");
    }
    else
    salida=true;
  }
  return(n);
}