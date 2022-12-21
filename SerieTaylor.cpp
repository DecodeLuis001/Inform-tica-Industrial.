//Serie de taylor
#include <iostream>
#include <iomanip>          //Necesaria para poder usar la funcion setpresicion() y trunc(), que son necesarias para calcular el indice de error.
#include <stdio.h>
#include <math.h>           //Para poder utilizar las funciones sen(x) y cos(x)
#include <ctime>            //Necesaria para usar la funcion clock()
#define PI 3.14159265

using namespace std;

//Se definen las variables globales.
int i, j, n;                                                               //Para los indices.
unsigned t0, t1;                                                          //Inician y temrinan el cronometraje.
double angulo, seno=0, coseno=0, dividendo, divisor, signo, error=0;     //Control de la serie de taylor.

//Prototipo de las funciones.
void TaylorSeno(double x);
void TaylorCoseno(double x);

int main()
{
    cout<<"--------> El numero maximo de iteraciones es: 750 <---------"<<endl;
    cout << "" << endl;
    printf("Introduce el valor de las iteraciones: ");
    scanf("%d", &n);

    if(n > 0 && n <=750)    
    {
        printf("Introduce el valor del angulo: ");
        scanf("%lf", &angulo);
        cout<<""<<endl;

        double x = angulo*PI/180;

        t0 = clock();       //Inicio del temporizador.
            TaylorSeno(x);
            cout<<"----------------------------------------------------------------------------"<<endl;
            TaylorCoseno(x);
            cout<<"----------------------------------------------------------------------------"<<endl;
        t1 = clock();       //Final del temporizador.

        double time = (double(t1-t0)/CLOCKS_PER_SEC);
        cout << "El tiempo de ejecucion del programa fue de: " << time << " ms" << endl;

    }
    else if(n == 0)
    {
        cout<<"Se requiere al mneos una iteracion para hacer el calculo."<<endl;
    }
    else
    {
        cout<<"Ha excedido el numero maximo de iteraciones."<<endl;
    } 

    return 0;
}

/*Notas importantes: 
Para un major manejo del dividendo y el divisor se emplea la forma: a += b
que equivale a = a + b para sintetizar el acumulador de la sumatoria.

La documentacion de la funcion TaylorSeno es igualmente aplicable a la funcion de TaylorCoseno.
La unica diferencia es que cambia la expresion del dividendo y divisor, pero el funcionamiento es igual.
*/

void TaylorSeno(double x)
{
    for(i=0; i<=n; i++)                 //Este ciclo es el encargado de generar la sumatoria.
    {
        dividendo = 1;
        for(j=0; j<((2*i)+1); j++)      //Se trabaja el dividendo iterativamente.
        {
            dividendo *= x;             //el acumulador se multiplica a si mismo junto al angulo iterativamente en funcion de n. 
        }
        divisor = 1;
        for(j = 1; j<=((2*i)+1); j++)   //Se trabaja el divisor iterativamente.
        {
            //Se hace un factorial: divisor = divisor * j
            divisor *= j;               //el acumulador se multiplica a el mismo pero tomando en cuenta el factorial del divisor iterativamente en funcion de n. 
        }
        //Para la parte del signo en la fomulacion en las series de Taylor, se debe recordar que:
        //Si el numero es par, la operacion del dividendo / divisor se multiplica por +1.
        //Si el numero es impar, la operacion del dividendo / divisor se multiplica por -1.
        if(i%2 == 0)
        {
            signo = 1;
        }
        else
        {
            signo = -1;
        }
        seno = seno + (dividendo / divisor) * signo;
    }
        
    cout << "Valores calculados para el seno: " << endl;
    cout << "Mediante la serie de Taylor: " << endl;
    printf("\t sin(%.2lf) = %.9lf\n", angulo, seno);
    cout << "Mediante math.h: " << endl;
    printf("\t sin(%.2lf) = %.6lf\n", angulo, sin(x));
    cout << "Indice de error por serie de Taylor y Trigonometria: " << endl;
    cout << setprecision(4) << "\t Error de seno = " << sin(x) - trunc(seno*1000)/1000.0 <<"..."<< endl;
    cout<<""<<endl;
}

void TaylorCoseno(double x)
{    
    for(i=0; i<=n; i++)
    {
        dividendo = 1;
        for(j=0; j<(2*i); j++)
        {
            dividendo *= x; 
        }
        divisor = 1;
        for(j = 1; j<=(2*i); j++)
        {
            divisor *= j;
        }
        if(i%2 == 0)
        {
            signo = 1;
        }
        else
        {
            signo = -1;
        }
        coseno += (dividendo / divisor) * signo;
    }
        
    cout << "Valores calculados para el coseno: " << endl;
    cout << "Mediante la serie de Taylor: " << endl;
    printf("\t cos(%.2lf) = %.9lf\n", angulo, coseno);
    cout << "Mediante math.h: " << endl;
    printf("\t cos(%.2lf) = %.6lf\n", angulo, cos(x));
    cout << "Indice de error por serie de Taylor y Trigonometria: " << endl;
    cout << setprecision(4) << "\t Error de coseno = " << cos(x) - trunc(coseno*1000)/1000.0 <<"..."<< endl;
    cout<<""<<endl;
}
