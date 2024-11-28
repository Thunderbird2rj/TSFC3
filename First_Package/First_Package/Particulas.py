class Particula:  # Se crea una clase llamada Particula
    def __init__(self, nombre, masa, carga):  # Argumentos que tomará la clase
        # Se definen los atributos que tomará en cuenta la clase
        self.nombre = nombre
        self.masa = masa
        self.carga = carga

    def info(self):
        return (f'Particula: {self.nombre} \n'  # Utiliza paréntesis para una mejor legibilidad
                f'Masa: {self.masa} \n'
                f'Carga: {self.carga}')



class Lepton1(Particula): #La calss lepton1 se utiliza para diferenciar las párticulas que son leptones pero tienen distintas propiedades de los otros
                                      #indica que lepton1 es un "objeto" de tipo partícula pero se le asignará propiedades agregadas a las de "Particula"
  def __init__(self, nombre, masa, carga, mommag, vm,logn_de_des, dipolo_electrico, dipolo_debil, neutrinos, anomalia, familia_leptonica):
    super().__init__(nombre, masa, carga) #llama al constrcutor de la clase para que detcte que los atributos deben ser los de tipo Particula
                                                                # y se inicialicen correctamente
    self.mommag = mommag
    self.vm = vm
    self.logn_de_des = logn_de_des
    self.dipolo_electrico = dipolo_electrico
    self.dipolo_debil = dipolo_debil
    self.neutrinos = neutrinos
    self.anomalia = anomalia
    self.familia_leptonica = familia_leptonica

  def info(self): #Con esta función se coloca el formato en el que se va a presentar la información de las instancias
    return(f'Particula: {self.nombre} \n'
          f'Masa (MeV/c^2): {self.masa} \n'
          f'Carga eléctrica (e): {self.carga} \n'
          f'Momento magnético anómalo (g − 2): {self.mommag} \n'
          f'Vida media (τ): {self.vm} \n'
          f'Longitud de desintegración (cτ): {self.logn_de_des} \n'
          f'Dipolo eléctrico (e·cm): {self.dipolo_electrico} \n'
          f'Dipolo débil (e·cm): {self.dipolo_debil} \n'
          f'Número de tipos de neutrinos: {self.neutrinos} \n'
          f'Anomalia magnética débil: {self.anomalia} \n'
          f'Violación de número de familia leptónica: {self.familia_leptonica} \n')



class Lepton2(Particula): #Se coloca una segunda clase para laptones con particularidades que el 1 no tiene
  def __init__(self, nombre, masa, carga, mommag, neutrinos, vidamedia, am12, am23, am13):
    super().__init__(nombre, masa, carga)
    self.mommag = mommag
    self.neutrinos = neutrinos
    self.vidamedia = vidamedia
    self.am12 = am12
    self.am23 = am23
    self.am13 = am13
  def info(self):
    return(f'Particula: {self.nombre} \n'
          f'Masa (eV/c^2): {self.masa} \n'
          f'Carga eléctrica (e): {self.carga} \n'
          f'Momento magnético (e·cm): {self.mommag} \n'
          f'Número de tipos de neutrinos: {self.neutrinos} \n'
          f'Vida media/másica (τ /m) (s/eV): {self.vidamedia} \n'
          f'Ángulo de mezcla θ_12: {self.am12} \n'
          f'Ángulo de mezcla θ_23: {self.am23} \n'
          f'Ángulo de mezcla θ_13: {self.am13} \n')


class Quark(Particula): #Se abre otra clase de partículas para los quarks
                        #se usan diferentes caracteristicas pero es la misma manera de hacer la estructura
  def __init__(self, nombre, masa, carga, isospin, sabor_ex, sabor_en, sabor_i, sabor_s, rmasa, gamma, decaimientos):
    super().__init__(nombre, masa, carga)
    self.nombre = nombre
    self.masa = masa
    self.carga = carga
    self.isospin = isospin
    self.sabor_ex = sabor_ex
    self.sabor_en = sabor_en
    self.sabor_i = sabor_i
    self.sabor_s = sabor_s
    self.rmasa = rmasa
    self.gamma = gamma
    self.decaimientos = decaimientos
  def info(self):
    return (f'Particula: {self.nombre} \n'
          f'Masa (MeV/c^2): {self.masa} \n'
          f'Carga eléctrica (e): {self.carga} \n'
          f'Isospin: {self.isospin} \n'
          f'Sabor extraño: {self.sabor_ex} \n'
          f'Sabor encantado: {self.sabor_en} \n'
          f'Sabor inferior: {self.sabor_i} \n'
          f'Sabor superior: {self.sabor_s} \n'
          f'Relación masa: {self.rmasa} \n'
          f'Ancho de desintegración (Γ): {self.gamma} \n'
          f'Decaimientos: {self.decaimientos} \n')


class Boson(Particula): #De la misma forma para los bosones, se crea una subclase y se colocan propiedades que se le agregarán
  def __init__(self, nombre, masa, carga, spin, ancho_desintegracion, modos_desintegracion, vidamed, afermiones, abosones):
    super().__init__(nombre, masa, carga)
    self.nombre = nombre
    self.masa = masa
    self.carga = carga
    self.spin = spin
    self.ancho_desintegracion = ancho_desintegracion
    self.modos_desintegracion = modos_desintegracion
    self.vidamed = vidamed
    self.afermiones = afermiones
    self.abosones = abosones
  def info(self):
    return (f'Particula: {self.nombre} \n'
          f'Masa (MeV/c^2): {self.masa} \n'
          f'Carga eléctrica (e): {self.carga} \n'
          f'Spin (J): {self.spin} \n'
          f'Ancho de desintegración (Γ): {self.ancho_desintegracion} \n'
          f'Modos de desintegración: {self.modos_desintegracion} \n'
          f'Vida media: {self.vidamed} \n'
          f'Acoplamiento con fermiones: {self.afermiones} \n'
          f'Acomplamiento con bosones: {self.abosones} \n')

