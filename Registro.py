from dataclasses import dataclass, fields

@dataclass
class Registro:
    name : str
    apellido1 :str
    apellido2 :str
    company : str
    cargo : str
    calle : str
    num_ext :int
    num_int :int
    colonia :str
    municipio :str
    estado :str
    zip_code :str
    phone : int
    email : str
    fecha_nacimiento :str    
    
    def __str__(self) -> str:
        return f""" 
        Nombre : {self.name}
        Apellido Paterno : {self.apellido1}            
        Apellido Materno : {self.apellido2}     
        Cargo : {self.cargo}
        Calle : {self.calle}
        Num Ext. : {self.num_ext}       
        Num int. : {self.num_int}       
        Colonia : {self.colonia}
        Minicipio : {self.municipio}
        Estado : {self.estado}
        Codigo Postal : {self.zip_code}
        Telefono : {self.phone}
        E-mail : {self.email}
        Fecha de nacimiento : {self.fecha_nacimiento}
        """