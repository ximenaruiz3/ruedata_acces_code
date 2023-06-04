import requests
class  DecodeKeys():

    @staticmethod
    def read_data():
        """
        Permite realizar una solicitud al url dado para obtener los datos
        del archivo keylog.txt

        Parameters
        ------
        Returns
        ------
        String

            retorna los datos del archivo en caso de que la solicitud haya sido exitosa
            de lo contrario retornara el status_code del error.

        Raises
        -------
        status code
            en caso de que la solicitud falle.
        """
        response = requests.get('https://rue-platform-dev.s3.amazonaws.com/keylog.txt')
        if response.status_code == 200:
            #verifica si la solicitud fue exitosa
            data = response.text 
            return data
        else:
            return  response.status_code

    def search_code(self):      
        """
        analiza los datos del archivo dado hasta conseguir el codigo de acceso.
        para determinar este, primero se consigue todos los números que implica el codigo.
        luego se empieza a analizar cada uno de ellos en los datos datos determinando asi
        que números se encuentran despues de el y metiendolos en un dicionario que contiene 
        la estructura
        {numero: numero de estudio, VECT: determina los números que 
            se encuentran por delante de él}
        luego se realiza un ordenamiento a estos diccionarios hasta determinar el 
        orden de los digitos.
        Parameters
        ----------
        Returns
        -------
            list
                lista de los numeros del codigo en su respectivo orden
        Raises
        ------
            
        """
        NUMBER = "number"
        VECT = "vect"
        data = self.read_data() #lectura de datos
        keys = data.split("\n") # eliminar caracteres 
        num_unique = list(set(data.replace("\n","")))
        less_than = []
        for num in num_unique:
            dict_num = {NUMBER:num, VECT:[]}
            for key in keys:
                if num in key and key != "\n":
                    idx_num = int(key.index(num))
                    for i in range(idx_num+1,len(key)):
                        if not key[i] in dict_num[VECT]:
                            dict_num[VECT].append(key[i])  
                    
            less_than.append(dict_num)
        order_by_len_vect = sorted(less_than,key=lambda x:len(x[VECT]), reverse= True)
        acces_code = list(map(lambda x: x[NUMBER], order_by_len_vect))
        return acces_code
                    
                
            