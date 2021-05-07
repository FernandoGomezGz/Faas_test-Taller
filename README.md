                                                          *Taller de Function as a Service*

Integrantes: Armando Tapia Meza
             Fernando Gomez Gonzalez
             Edgar Piña Cuentas
             

Funciones Integradas en el programa

FindByPrescription: La función hace una busqueda entre los fármacos, mostrando en la web los productos que tienen prescripción medica o no. Si un medicamento tiene prescripcion 
se identifica con un 1 y si no tiene se identifica con un 0.

AggItem: La función agrega un producto al stock de los medicamentos disponibles. La función requiere los siguientes parametros para completar la solicitud de adición:
  <id>
  <stock>
  <imageUrl>
  <name>
  <price>
  <prescription>
  
Delet: La función borra un producto que esté disponible o existente en el inventario de medicamentos, esta hace una búsqueda con el parámetro <id> que es pedido al usuario.



https://faastaller.azurewebsites.net/findbyprescription?prescription=0
https://faastaller.azurewebsites.net/aggitem?id=1002&stock=1000&imageUrl=1212&name=cocalcoal&price=3000&prescription=1
https://faastaller.azurewebsites.net/delete?id=1
