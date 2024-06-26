#Tiempo
import time

#Bienvenida 
def main():
    while True:
        print("Hola! Bienvenido a Calfún School");
        time.sleep(1);
        print("Este es el menú de opciones!");
        time.sleep(1);
        #Menú de opciones
        print("1.- Agregar un estudiante.");
        print("2.- Ver todos los estudiantes.");
        print("3.- Modificar un estudiante.");
        print("4.- Eliminar un estudiante.");
        print("5.- Guardar colección en un archivo");
        print("6.- Salir del programa.");
        try:
            opcion=int(input("Ingrese el número de la opción --->"));

            if opcion==1:
                print("Opción 1- Agregar un estudiante.");
                time.sleep(1);
                #funcion
            
            elif opcion==2:
                print("Opción 2- Ver todos los estudiantes.");
                time.sleep(1);
                #funcion
            
            elif opcion==3:
                print("Opción 3- Modificar un estudiante.");
                time.sleep(1);
                #funcion
            
            elif opcion==4:
                print("Opción 4- Eliminar un estudiante.");
                time.sleep(1);
                #funcion
            
            elif opcion==5:
                print("Opción 5- Guardar colección en un archivo.");
                time.sleep(1);
                #funcion

            elif opcion==6:
                print("Opción 6- Salir del programa.");
                time.sleep(1);
                print("Saliendo del programa...");
                time.sleep(2);
                break;
            else:
                print("ERROR- Ingrese un número del menú de opciones , vuelva a intentarlo.")
        except ValueError:
            print("ERROR- Ingrese un número, vuelva a intentarlo.")
            
        
main()


def agregarAlumno():
    nombreAlumno=input("Nombre: ")
    edadAlumno=input("Edad: ")
    cursoAlumno=input("Curso: ")
    promedioAlumno=input("Promedio: ")

    listaAlumnos.append([nombreAlumno,edadAlumno,cursoAlumno,promedioAlumno])
    print("Se agrego el alumno correctamente")



def guardarAlumnos():
    with open ('Alumnos.txt','w', encoding='utf-8') as archivo:
        archivo.write(listaAlumnos)



