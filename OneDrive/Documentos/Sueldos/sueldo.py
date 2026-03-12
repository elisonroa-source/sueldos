# ==========================================
# CALCULO DE SUELDO NETO EN REPUBLICA DOMINICANA
# ==========================================

PORC_TSS = 0.0591   # 5.91%

# Escala anual DGII convertida a mensual
LIMITE_EXENTO = 416220 / 12
LIMITE_TRAMO2 = 624329 / 12
LIMITE_TRAMO3 = 867123 / 12

CUOTA_TRAMO3 = 31216 / 12
CUOTA_TRAMO4 = 79776 / 12


# -------- FUNCIONES --------

def calcular_isr(base):
    if base <= LIMITE_EXENTO:
        return 0
    elif base <= LIMITE_TRAMO2:
        return (base - LIMITE_EXENTO) * 0.15
    elif base <= LIMITE_TRAMO3:
        return CUOTA_TRAMO3 + ((base - LIMITE_TRAMO2) * 0.20)
    else:
        return CUOTA_TRAMO4 + ((base - LIMITE_TRAMO3) * 0.25)


def calcular_bonificacion(sueldo, años):
    salario_diario = sueldo / 30

    if años < 3:
        return salario_diario * 45
    else:
        return salario_diario * 60


# -------- PROGRAMA --------

print("====================================")
print(" CALCULO DE SUELDO NETO EN RD")
print("====================================")

sueldo_bruto = float(input("Ingrese el sueldo bruto mensual: "))

if sueldo_bruto <= 0:
    print("ERROR: El sueldo debe ser mayor que 0")

else:

    otros_descuentos = float(input("Ingrese otros descuentos: "))
    años = int(input("Años trabajando en la empresa: "))

    boni = input("¿Recibe bonificación? (si/no): ").lower()
    doble = input("¿Recibe doble sueldo? (si/no): ").lower()

    # TSS
    descuento_tss = sueldo_bruto * PORC_TSS

    # Base ISR
    base_isr = sueldo_bruto - descuento_tss

    # ISR mensual
    retencion_isr = calcular_isr(base_isr)

    # Bonificación
    if boni == "si":
        bonificacion = calcular_bonificacion(sueldo_bruto, años)
    else:
        bonificacion = 0

    # Doble sueldo
    if doble == "si":
        doble_sueldo = sueldo_bruto
    else:
        doble_sueldo = 0

    # SUELDO NETO FINAL
    sueldo_neto = sueldo_bruto - descuento_tss - retencion_isr - otros_descuentos + bonificacion + doble_sueldo

    print("\n=========== RESULTADOS ===========")
    print(f"Sueldo Bruto: RD$ {sueldo_bruto:,.2f}")
    print(f"Descuento TSS: RD$ {descuento_tss:,.2f}")
    print(f"Retención ISR: RD$ {retencion_isr:,.2f}")
    print(f"Otros Descuentos: RD$ {otros_descuentos:,.2f}")
    print(f"Bonificación: RD$ {bonificacion:,.2f}")
    print(f"Doble Sueldo: RD$ {doble_sueldo:,.2f}")
    print(f"Sueldo Neto: RD$ {sueldo_neto:,.2f}")