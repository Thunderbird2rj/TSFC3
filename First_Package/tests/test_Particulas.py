# test_particulas.py

from First_Package.Particulas import Lepton1, Lepton2, Quark, Boson

def test_lepton1():
    # Crear Lepton1
    electron = Lepton1(
        nombre='Electron',
        masa="0.51099895000±0.00000000015",
        carga=-1,
        mommag="(1159.65218062±0.00000012)e-6",
        vm='>6.6e-28 años',
        logn_de_des="-",
        dipolo_electrico='<0.041e-28',
        dipolo_debil='-',
        neutrinos=3,
        anomalia='-',
        familia_leptonica='-'
    )
    assert electron.nombre == 'Electron'
    assert electron.masa == "0.51099895000±0.00000000015"
    assert electron.carga == -1
    assert electron.mommag == "(1159.65218062±0.00000012)e-6"
    assert electron.vm == '>6.6e-28 años'
    assert electron.logn_de_des == "-"
    assert electron.dipolo_electrico == '<0.041e-28'
    assert electron.dipolo_debil == '-'
    assert electron.neutrinos == 3
    assert electron.anomalia == '-'
    assert electron.familia_leptonica == '-'
    print("Lepton1 test passed.")

def test_lepton2():
    # Crear Lepton2
    Neutrino_electron = Lepton2(
        nombre='Neutrino electrón ν_e',
        masa= "<0.8",
        carga=0,
        mommag="<0.064e-10",
        neutrinos=3,
        vidamedia=">300",
        am12="0.307 ± 0.013",
        am23="0.553 ± 0.016",
        am13="0.0219 ± 0.0007"
    )
    assert Neutrino_electron.nombre == 'Neutrino electrón ν_e'
    assert Neutrino_electron.masa == "<0.8"
    assert Neutrino_electron.carga == 0
    assert Neutrino_electron.mommag == "<0.064e-10"
    assert Neutrino_electron.neutrinos == 3
    assert Neutrino_electron.vidamedia == ">300"
    assert Neutrino_electron.am12 == "0.307 ± 0.013"
    assert Neutrino_electron.am23 == "0.553 ± 0.016"
    assert Neutrino_electron.am13 == "0.0219 ± 0.0007"
    print("Lepton2 test passed.")

def test_quark():
    # Crear Quark
    Up = Quark(
        nombre ="Up (u)",
        masa = "2.16± 0.07",
        carga = "+2/3",
        isospin = "I = 1/2, I_z = +1/2",
        sabor_ex= 0,
        sabor_en= 0,
        sabor_i= 0,
        sabor_s= 0,
        rmasa= "m_u/m_d = 0.462 ± 0.020",
        gamma= "-",
        decaimientos= "-"
    )
    assert Up.nombre == "Up (u)"
    assert Up.masa == "2.16± 0.07"
    assert Up.carga == "+2/3"
    assert Up.isospin == "I = 1/2, I_z = +1/2"
    assert Up.sabor_ex == 0
    assert Up.sabor_en == 0
    assert Up.sabor_i == 0
    assert Up.sabor_s == 0
    assert Up.rmasa == "m_u/m_d = 0.462 ± 0.020"
    assert Up.gamma == "-"
    assert Up.decaimientos == "-"
    print("Quark test passed.")

def test_boson():
    # Crear Boson
    Higgs = Boson(
        nombre ="Higgs (H)",
        masa = "125.20 ± 0.11",
        carga= "0",
        spin = 0,
        ancho_desintegracion = "3.7^{+1.9}_{−1.4} MeV",
        modos_desintegracion = "bb̄ (53%), WW∗ (25.7%)",
        vidamed = "-",
        afermiones = "κ_F = 0.94 ± 0.05",
        abosones = "κ_V = 1.023 ± 0.026"
    )
    assert Higgs.nombre == "Higgs (H)"
    assert Higgs.masa == "125.20 ± 0.11"
    assert Higgs.carga == "0"
    assert Higgs.spin == 0
    assert Higgs.ancho_desintegracion == "3.7^{+1.9}_{−1.4} MeV"
    assert Higgs.modos_desintegracion == "bb̄ (53%), WW∗ (25.7%)"
    assert Higgs.vidamed == "-"
    assert Higgs.afermiones == "κ_F = 0.94 ± 0.05"
    assert Higgs.abosones == "κ_V = 1.023 ± 0.026"
    print("Boson test passed.")

if __name__ == "__main__":
    test_lepton1()
    test_lepton2()
    test_quark()
    test_boson()
    print("All tests passed.")
