<sub>🌐 <a href="README.md">简体中文</a> · <a href="README.zh-Hant.md">繁體中文</a> · <a href="README.en.md">English</a> · <a href="README.fr.md">Français</a> · <b>Español</b> · <a href="README.ar.md">العربية</a> · <a href="README.ja.md">日本語</a> · <a href="README.ru.md">Русский</a></sub>

<div align="center">

<img src="logo.png" alt="Hui Ning IP" width="150">

# Madrid Trademark · Sistema de Madrid

> *«Una sola pregunta. Una respuesta lista para el expediente.»*
> *"Ask once. Get a filing-ready Madrid practice answer."*

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-3.4.5-blue.svg)](https://github.com/huiningip/madrid-trademark)
[![Agent-Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet)](#instalación)
[![Madrid Members](https://img.shields.io/badge/Madrid%20Members-117%20%C2%B7%20133%20countries-green)](https://www.wipo.int/en/web/madrid-system/members/)
![Office-Neutral](https://img.shields.io/badge/Perspective-Office--Neutral-orange)

<br>

**Una habilidad de agente dedicada a la práctica del Sistema de Madrid, dirigida a agentes de marcas, abogados de propiedad intelectual y asesores jurídicos internos de todo el mundo.**

<br>

No es una divulgación sobre «qué es el Sistema de Madrid», sino **entregables que van directos al expediente**: liquidaciones de tasas exactas, cálculo de las dos categorías de plazos, listas de verificación y notas de respuesta listas para cumplimentar, y textos de tratados verificables palabra por palabra.

La fase internacional de la OMPI es idéntica desde cualquier Parte Contratante. Esta habilidad está redactada con una **perspectiva neutral (office-neutral)** — el apartado CNIPA/China es solo un capítulo opcional. Parta usted de la USPTO, la EUIPO, la JPO o la CNIPA, el uso es el mismo.

Cada importe de tasa, cada plazo y cada declaración lleva **fecha de corte de los datos y punto de verificación oficial**. Lo que no se encuentra se responde con «ninguno» — sin inventar.

```
git clone https://github.com/huiningip/madrid-trademark ~/.workbuddy/skills/madrid-trademark
```

Compatible con cualquier agente — se instala en todo agente que admita skills.

> 📣 **Los datos volátiles nunca se fijan en duro.** Tasas, tasas individuales, declaraciones de las Partes Contratantes, número de miembros y textos jurídicos llevan cada uno «fecha de corte + periodicidad de revisión + punto de verificación oficial». Al vencer, la habilidad exige verificación en línea y rechaza fiarse de los valores en caché de los buscadores.

[Qué hace](#qué-hace) · [Instalación](#instalación) · [Mecanismos clave](#mecanismos-clave) · [Estructura del repositorio](#estructura-del-repositorio) · [Limitaciones](#limitaciones)

</div>

---

<p align="center"><sub>

```
Solicitud/registro de base ──▶ Remisión por la oficina de origen ──▶ Examen formal OMPI ──▶ Fecha de registro internacional
                                                                                              │
                                          ┌───────────────────────────────────────────────────┴──────────────────────────┐
                                          ▼                                                                              ▼
                  Plazo de denegación por oficina designada: 12 / 18 / 25 meses              Ataque central: dependencia de 5 años
                                          │                                                                              │
                          Sin denegación ⇒ protección concedida                Base anulada ⇒ transformación en 3 meses,
                                                                              presentada directamente ante cada oficina designada
```

</sub></p>

<p align="center"><sub>▲ Un único hilo conductor: solicitud → remisión → seguimiento de los plazos de denegación → repliegue por transformación. Cada punto de control 🔴 queda bloqueado por la habilidad.</sub></p>

---

## Instalación

```bash
# Opción 1: CLI de skills
npx skills add huiningip/madrid-trademark

# Opción 2: git clone (alternativa si la sincronización de la CLI falla)
git clone https://github.com/huiningip/madrid-trademark ~/.workbuddy/skills/madrid-trademark
```

> **Compruebe tras instalar**: no es una habilidad reducida a `SKILL.md`. `references/` (13 archivos Markdown + 2 PDF oficiales), `scripts/` (7 scripts Python + 2 archivos JSON de datos) y `templates/` (2 plantillas) son entidades referenciadas en el cuerpo del texto mediante rutas relativas `@`; basta con que falte una para romper la cadena.
>
> Tras instalar, revise el directorio: si solo aparece `SKILL.md` y faltan los subdirectorios, su herramienta de sincronización capturó un solo archivo — reinstale con `git clone` como arriba.
>
> Autoprueba de los scripts (Python 3.10+; los scripts sin conexión usan solo la biblioteca estándar):
>
> ```bash
> py -B scripts/selftest.py     # 9 grupos de casos — todo en verde = despliegue completo
> ```

Después, hable directamente con el agente, en cualquier agente compatible con skills:

```
«Tasa individual para Japón: calcúlame una solicitud de 3 clases»
«Denegación para China: ¿15 o 30 días, y desde cuándo se cuentan?»
«El registro de base de mi cliente (2021) acaba de ser anulado: ¿aún cabe transformación?»
«Renovación: registrado el 2016-07-01 por 10 años. ¿Todavía estoy a tiempo?»
«Calcula los plazos de denegación para US/JP/ID/IL — ¿cuáles exigen vigilancia a 18 meses?»
```

Sin formularios. Sin asistentes paso a paso. Sin registro. Una pregunta y obtiene material para el expediente.

---

## Qué hace

| Capacidad | Entregable | Restricción clave |
|-----------|------------|-------------------|
| Solicitud internacional | Pasos del procedimiento + `templates/madrid_application_checklist.md` | Bloquea el plazo de remisión (2 meses) y las especificaciones de reproducción |
| Cálculo de tasas | Liquidación por Parte (tasa básica / suplementaria / complementaria / individual) | **Doble control**: instantánea sin conexión vs medición oficial en vivo |
| Cálculo del plazo de denegación | Cuenta atrás de 12 / 18 / 25 meses | Verificar primero las declaraciones de la Parte — **nunca presumir 18 meses** |
| Cálculo del plazo de respuesta | Cuenta atrás por Parte (incluida China 15 / 30 días) | Reconoce 6 puntos de inicio; **rechaza** contar desde la fecha de recepción si la base oficial difiere |
| Respuesta a la denegación provisional | Calificación del procedimiento + ejes de estrategia + `templates/madrid_refusal_response_memo.md` | Distinguir primero la denegación de oficio de la oposición de un tercero |
| Gestión de la renovación | Ventana de renovación + recargo por plazo de gracia | Recargo de gracia = **50 % de la tasa básica (327 CHF)** |
| Modificación / cesión / limitación / renuncia | Vía de presentación + reglas de número (número de origen + letra mayúscula) | División y fusión pasan por la oficina de origen |
| Respuesta al ataque central | Test de dependencia de 5 años + cuenta atrás de 3 meses | La transformación se presenta **directamente ante cada oficina designada**, no ante la OMPI |
| Verificación de productos/servicios (MGS) | Proceso de cotejo del enunciado normalizado | El enunciado debe coincidir exactamente con la MGS de la OMPI |
| Examen de declaraciones | Lista por Parte de las 17 categorías + test de la cláusula de salvaguardia | Las declaraciones pueden ser **ineficaces** entre Estados doblemente partes |
| Apartado China (CNIPA) | Vía de presentación por la oficina de origen + puntos del examen acelerado | Capítulo opcional — prescindible fuera de la práctica china |
| Verificación de tratados | Textos íntegros y literales del Arreglo / Protocolo / Reglamento / Instrucciones | Citar siempre el cuerpo del texto, nunca el resumen |

---

## Cobertura en detalle

### Tasas: dos vías, no sustituibles entre sí

`scripts/madrid_fee.py` es el cálculo por **instantánea sin conexión** — sin red ni navegador, con las tasas individuales de 76 Partes Contratantes integradas; aplica las **modificaciones tarifarias anunciadas** según `--date`.

`scripts/madrid_feecalc_live.py` es la **medición oficial en vivo** — maneja la Calculadora de Tasas de la OMPI con un navegador real, devuelve los importes autorizados por Parte y constituye el instrumento dirimente cuando se discute un importe.

> La calculadora oficial es una aplicación JSF: tanto la lista de Partes como los resultados se renderizan por JavaScript, lo que la hace **imposible de capturar por HTTP simple**. Cada casilla marcada provoca un repintado AJAX y un clic aislado puede perderse; por eso el script reintenta hasta 4 rondas («marcar → releer el conjunto marcado → marcar lo que no prendió»). Si la línea final indica «N / M marcadas» por debajo de M, el resultado es inutilizable por diseño.

```bash
# Sin conexión: primera estimación para un presupuesto
py madrid_fee.py --countries ID,IL --classes 2 --date 2026/11/01

# En vivo: la medición decisiva cuando se discute un importe
py madrid_feecalc_live.py --origin US --classes 1 --countries JP,ID,IL
```

**`--date` es el parámetro decisivo.** La página de tasas individuales de la OMPI solo muestra el importe *actual*, mientras que la calculadora aplica las tarifas vigentes en la *fecha de presentación prevista*. Al cruzar una fecha de entrada en vigor (habitualmente el 1 de noviembre o el 1 de enero), hay que cifrar por separado según la fecha de presentación prevista — una misma solicitud puede tener dos precios a uno y otro lado. Ejemplo medido y registrado: **entrada en vigor el 2026-11-01, Indonesia 91 → 125, Israel 471 → 503**.

### Plazos: dos categorías, y aquí es donde falla la práctica

El **plazo de denegación** es el plazo de la *oficina* para notificar, contado en meses: base de **12 meses**, **18 meses** cuando la Parte ha formulado la declaración del artículo 5(2)(b), y hasta unos **25 meses** cuando se añade una declaración del artículo 5(2)(c) y surge una oposición. En un designación posterior corre desde la **fecha de inscripción**.

El **plazo de respuesta** es el plazo del *titular* para contestar una denegación provisional, contado en días o meses, notificado país por país conforme a la regla 17(7):

- China (CN): **15 días** para denegación de oficio / **30 días** para denegación por oposición, desde la recepción de la remisión de la OMPI
- Francia (FR): 1 mes / 2 meses · Reino Unido (GB): 2 meses · Alemania (DE): 4 meses · Japón (JP): 3 meses
- Estados Unidos (US): 6 meses (de oficio) / 40 días (oposición, desde el auto del TTAB) · Tailandia (TH): 90 días

> **Advertencia sobre la cobertura.** Esa tabla de la OMPI solo recoge **38 miembros** (de 117), y el punto de inicio varía según **6 modalidades** (recepción por el titular / remisión de la OMPI / envío por la oficina / recepción por la OMPI / día 14 tras el envío / auto del TTAB). **No figurar ≠ carecer de plazo de respuesta.** Cuando la base oficial no es «fecha de recepción», `madrid_deadline.py` **rechaza** contar desde la fecha de recepción —ese cálculo sobrestima el tiempo restante— y exige la fecha de inicio oficial.

**No confunda 15/30 días con 12/18/25 meses.** Los primeros son el plazo de respuesta del titular; los segundos, el plazo de notificación de la oficina.

### Ataque central: 3 meses, y al destinatario correcto

Un registro internacional depende de la solicitud/registro de base durante sus **5 primeros años**; si la base se anula, cae con ella. El remedio es el artículo 9quinquies: presentar una solicitud de transformación **directamente ante cada oficina designada** dentro de los **3 meses** siguientes a la anulación. La solicitud nacional resultante conserva la **fecha de registro internacional y la fecha de prioridad** originales.

> El error recurrente: presentar la transformación ante la OMPI. La transformación se presenta ante las **oficinas designadas**, no ante la Oficina Internacional.

### Declaraciones: verificar primero, decidir después

Las Partes Contratantes pueden formular 17 categorías de declaraciones y notificaciones, que inciden en la eficacia, las tasas y los plazos. Al elegir Partes designadas, verifique en orden: ¿percibe tasa individual? → ¿qué escalón de plazo de denegación? → ¿algún requisito especial (declaración de intención de uso, por ejemplo)? → ¿división/fusión aplicables? → ¿la inscripción de una licencia tiene eficacia internacional?

> **Recordatorio de la cláusula de salvaguardia.** Cuando la Parte designada **y** la Parte de origen son **ambas partes en el Arreglo y en el Protocolo**, las declaraciones de ese Estado conforme al artículo 8(7) y al artículo 5(2)(b)/(c) son **ineficaces en sus relaciones mutuas** (artículo 9sexies(1)(b) del Protocolo; partidas 2.4 / 5.3 / 6.4 del Arancel de Tasas). Un solicitante chino que designe Francia, Alemania, Italia, España o Suiza debe verificar este punto caso por caso.

### Textos de los tratados: verificables palabra por palabra, reextraíbles con un comando

El Arreglo (18 artículos), el Protocolo (16 artículos + 10 subreglas), el Reglamento (41 reglas + Arancel de Tasas) y las Instrucciones Administrativas (7 partes, 19 secciones + sección 11bis) se incluyen como **textos íntegros y literales en chino** (traducción oficial de WIPO Lex) emparejados con los **textos oficiales en inglés**. Cuando la OMPI actualice un texto, reextráigalo con `wipo_lex_fetch.py`:

```bash
# Inspeccionar primero la estructura y verificar el primer y último artículo y su recuento
py -B wipo_lex_fetch.py --url https://www.wipo.int/wipolex/en/text/384637 --inspect
```

---

## Mecanismos clave

### La compuerta de frescura de los datos volátiles

La regla más dura de la habilidad. Todo lo que puede cambiar —tasas, tasas individuales, declaraciones, número de miembros, tipos de cambio, versiones de los tratados— debe figurar en el §3.0 con «fecha de corte + periodicidad de revisión + punto de verificación oficial»:

| Dato | Fecha de corte | Revisión | Punto de verificación |
|------|----------------|----------|------------------------|
| Número de miembros | 2026-09-23 | Mensual | Página de miembros de la OMPI |
| Tasas de la OMPI | Arancel, versión 2023-02-01 | Trimestral | Arancel de Tasas de la OMPI |
| Tasa individual por Parte | 2026-08-23 | Mensual | Página de tasas individuales |
| Declaraciones de las Partes | 2026-03-15 | Mensual | Página de declaraciones |
| Tabla de plazos de respuesta | 2026-08-28 | Mensual | Página de plazos de respuesta |
| Tipo de cambio del CHF | **no integrado** | Antes de cada pago | Tipo en tiempo real / Fee Calculator |

Vencida la periodicidad, o a petición expresa del usuario, la habilidad **debe verificar en línea antes de responder**. Lo que no se encuentra recibe la respuesta «ninguno».

### Fuente única por dato

Un mismo dato nunca se almacena en dos sitios, lo que evita la coexistencia de dos versiones:

- Tasas → `references/madrid-fees.md` (espejo legible por máquina: `scripts/madrid_fee_data.json`)
- FAQ y contraejemplos → `references/madrid-faq.md`
- Declaraciones → `references/madrid-declarations.md` (17 categorías numeradas)

La coherencia de cada par «versión humana ↔ versión máquina» la controlan casos dedicados de `selftest.py` Parte por Parte — modifique el documento sin sincronizar el dato y la autoprueba se pone en rojo.

### Dos categorías de plazos, estrictamente separadas

Un solo comando cubre ambas, con lógica estanca:

- El modo por defecto calcula el **plazo de denegación** (12 / 18 / 25 meses) — presume 12 meses y exige verificar las declaraciones; **18 meses requiere un `--declared-18` explícito**; invocar la prórroga por oposición sobre la base de 12 meses se rechaza de plano (el artículo 5(2)(c) presupone una declaración a 18 meses).
- `--respond` calcula el **plazo de respuesta** — datos de la regla 17(7) integrados para los 38 miembros, con resolución de las 6 modalidades de inicio.

### Disciplina de formato de salida

La documentación interna de la habilidad puede apoyarse en tablas Markdown; en cambio, **el texto entregado al usuario tras la llamada no debe contener tablas Markdown** — usa líneas «concepto: importe (base jurídica)», viñetas `·` por Parte o alineación por sangría. Ningún importe ni plazo pierde su unidad o su base; todo dato volátil se señala como pendiente de reverificación.

### Biblioteca de contraejemplos

`references/madrid-faq.md` recoge 16 contraejemplos frecuentes, incluidas las correcciones de errores históricos de esta habilidad. Entre los más frecuentes y dañinos: presumir un plazo de denegación de 18 meses; confundir tasa complementaria y tasa individual; calcular el recargo de gracia como «50 % del total debido»; pagar el último día del plazo de gracia; modificar la lista de productos durante la renovación; presentar la transformación ante la OMPI tras un ataque central.

> Principio de fondo: en la práctica de Madrid, **el cumplimiento de los plazos y la conformidad formal pesan más que la fuerza de la argumentación**. Un plazo perdido equivale, por regla general, a un derecho irrecuperable.

---

## Frente a una IA generalista

Pregunte a un modelo generalista «cuánto cuestan las tasas de Madrid» y obtendrá una cifra **sin fecha de corte, sin fuente trazable y posiblemente caducada**. La diferencia estriba en tres puntos:

| | IA generalista | madrid-trademark |
|---|---|---|
| Importes de tasas | Instantánea de los datos de entrenamiento, sin fecha de corte | Fecha de corte + punto de verificación oficial + remedición en vivo |
| Plazo de denegación | Suele responder «18 meses» | Base de 12 meses, dictada por las declaraciones; 25 meses con condiciones estrictas |
| Dato ausente | Tiende a inventar una respuesta verosímil | Responde «ninguno» |
| Cálculo de plazos | Mental, propenso a error | `madrid_deadline.py` resuelve las 6 modalidades de inicio |
| Citas jurídicas | Reformuladas, no verificables | Textos íntegros del Arreglo / Protocolo / Reglamento / Instrucciones, verificables con grep |
| Entregable | Un párrafo de prosa | Lista de verificación + nota de respuesta + desglose por Parte |

La IA generalista es una **mejor conversación**; esta habilidad busca **hacer desaparecer la incertidumbre del «no lo encuentro / no lo acierto»**.

---

## Datos y procedencia

- **Cero invención.** Lo que no se encuentra recibe la respuesta «ninguno» — nunca se estima ni se rellena con texto de relleno.
- **Sin telemetría.** La habilidad es un conjunto de archivos puramente local: no emite nada y no contiene claves.
- **Citas verificables.** Todos los textos de tratados proceden de páginas oficiales de WIPO Lex, y el script de extracción `wipo_lex_fetch.py` se distribuye para permitir la reextracción y la contraverificación. Los anexos «puntos clave y errata» son síntesis de la habilidad, no textos oficiales: **cite siempre el cuerpo del texto**.
- **Reproducible.** Todos los scripts de cálculo de fechas admiten `--today` para reproducción, lo que hace trazables los resultados.
- **Aviso.** La salida de los scripts es una estimación y una alerta; prevalecen la notificación oficial de la OMPI / la CNIPA y la factura oficial.

---

## Limitaciones

Lo que la habilidad no hace, dicho con franqueza:

- **No cubre la interpretación artículo por artículo del derecho sustantivo de marcas de las Partes designadas, ni las estrategias de litigio.** El derecho nacional (disposiciones concretas de la Lanham Act estadounidense, reglamento de la marca de la UE, práctica nacional de recurso) corresponde al derecho local o a un abogado local.
- **No tramita solicitudes nacionales o regionales.** Las presentaciones directas ante la USPTO, la EUIPO o la JPO, fuera de la vía de Madrid, quedan fuera del flujo principal y solo aparecen como comparación.
- **No emite juicios subjetivos de similitud ni pronósticos de éxito.** Aporta un marco de respuesta a la denegación y plantillas; no predice la registrabilidad, el riesgo de conflicto ni el resultado de un caso.
- **No extrae tipos de cambio en vivo.** El tipo del CHF es volátil y debe verificarse antes de cada pago.
- **No sustituye el juicio profesional.** Es una ayuda a la práctica, no un dictamen jurídico.
- **Sin el expediente no puede dar un plan específico.** Facilite primero la notificación de denegación, el número de registro y las Partes designadas.

**Para obtener la mejor respuesta:** indique el tipo de operación (solicitud / renovación / respuesta a denegación / modificación o cesión / transformación / tasas / plazos) + los hechos clave (Partes designadas, número de clases, situación de la base, fecha o número de registro, si hay denegación y de qué país) + el entregable esperado (estimación de tasas / cuenta atrás / plantilla de respuesta / pasos / lista de riesgos).

---

## Estructura del repositorio

```
madrid-trademark/
├── SKILL.md                          # Documento principal (lo lee el agente; estructura en seis partes: rol / tarea / contexto / proceso / reglas / formato de salida)
├── README.md                         # Chino simplificado (por defecto)
├── README.zh-Hant.md                 # Chino tradicional
├── README.en.md                      # English
├── README.fr.md                      # Français
├── README.es.md                      # Español (este archivo)
├── README.ar.md                      # العربية
├── README.ja.md                      # 日本語
├── README.ru.md                      # Русский
├── LICENSE                           # Licencia MIT
├── logo.png                          # Marca de la empresa (cabecera del README)
├── references/                       # 15 elementos: 13 Markdown + 2 PDF oficiales
│   ├── madrid-agreement.md / -en.md           # Arreglo de Madrid (18 artículos, texto íntegro zh/en)
│   ├── madrid-protocol.md / -en.md            # Protocolo de Madrid (16 artículos + 10 subreglas, zh/en)
│   ├── madrid-regulations.md / -en.md         # Reglamento (41 reglas + notas oficiales, zh/en)
│   ├── madrid-admin-instructions.md / -en.md  # Instrucciones Administrativas (7 partes, 19 secciones + 11bis, zh/en)
│   ├── madrid-fees.md                         # Fuente única de las tasas (tasas individuales de 76 Partes)
│   ├── madrid-declarations.md                 # Fuente única de las declaraciones (17 categorías + plazos de respuesta de 38 miembros)
│   ├── madrid-faq.md                          # FAQ + 16 contraejemplos + índice de artículos
│   ├── madrid-goods-services-classification.md    # Síntesis de la guía de clasificación (5.ª ed., 2026)
│   ├── madrid-fast-track-examination-cnipa.md     # Examen acelerado de la CNIPA: puntos prácticos
│   ├── madrid-efiling-applicant-guide.pdf         # Guía del solicitante e-Filing de la OMPI (oficial, 43 p.)
│   └── madrid-goods-services-classification-guide.pdf  # Guía oficial de clasificación (5.ª ed.)
├── scripts/                          # 9 elementos: 7 Python + 2 JSON
│   ├── madrid_fee.py                 # Calculadora de tasas (instantánea sin conexión; --date aplica las entradas en vigor)
│   ├── madrid_fee_data.json          # Espejo máquina de las tasas (alineado Parte por Parte con madrid-fees.md)
│   ├── madrid_deadline.py            # Calculadora de plazos (denegación 12/18/25 meses + respuesta, 38 miembros)
│   ├── madrid_response_times.json    # Datos de plazos de respuesta (tabla completa de la regla 17(7) + 6 inicios)
│   ├── madrid_renewal.py             # Ventana de renovación y recargo de gracia
│   ├── madrid_feecalc_live.py        # Medición de tasas en vivo (navegador sobre la calculadora oficial; herramienta dirimente)
│   ├── wipo_lex_fetch.py             # Extracción literal de tratados de WIPO Lex (a Markdown)
│   ├── madrid_dateutil.py            # Utilidades de fechas compartidas (mes natural, fin de mes, año bisiesto)
│   └── selftest.py                   # 9 grupos de autopruebas (incluidas dos comprobaciones de coherencia)
└── templates/                        # Copiar antes de usar; no modificar los originales in situ
    ├── madrid_application_checklist.md      # Lista de autocomprobación previa a presentar el MM2
    └── madrid_refusal_response_memo.md      # Nota de respuesta a la denegación provisional
```

> **Regla de estructura.** Estrictamente 2 niveles (nivel 1 = `SKILL.md` / `references/` / `scripts/` / `templates/`; nivel 2 = archivos de cada directorio), sin anidamiento más profundo.
> **Codificación.** Los archivos Markdown son CRLF puro, sin BOM; los `.py` y `.json` de `scripts/` son LF, UTF-8 sin BOM.
> **Disciplina de mantenimiento.** Toda modificación de un importe de tasa debe repercutirse en `references/madrid-fees.md` y `scripts/madrid_fee_data.json`, y `py scripts/selftest.py` debe superar todos los casos antes del commit.

---

## Origen

La dificultad de un expediente de Madrid es muy concreta: **lo mismo está escrito una vez en el Arreglo, otra en el Reglamento, otra en el Arancel de Tasas y otra más en las declaraciones de cada Parte Contratante** — y la revisión de cualquiera de ellos puede invalidar de golpe una posición que la semana anterior aún era correcta. Un cambio tarifario, una declaración más, un nuevo miembro: en la práctica, obliga a reverificarlo todo.

De ahí extraer las cuatro capas de textos jurídicos (Arreglo / Protocolo / Reglamento / Instrucciones Administrativas), junto con el Arancel, la página de declaraciones y las guías oficiales, en textos íntegros; sellar con fecha de frescura todos los datos volátiles; y escribir en scripts reproducibles todo lo calculable —plazos, tasas. El objetivo: convertir la «verificación» en una llamada, y no en una tarde entera.

---

## License

Publicado bajo **licencia MIT** ([LICENSE](LICENSE)). Puede **usar, modificar y distribuir** este proyecto, **incluso con fines comerciales** — uso interno, entrega en un expediente de cliente, obras derivadas y redistribución, sin autorización previa, sin coste y sin aviso. La atribución no es obligatoria, pero se agradece.

Copyright **Hui Ning IP (辉宁知识产权)**.

**Alcance.** La licencia MIT cubre el código (`scripts/`) y la documentación propios de esta habilidad (`SKILL.md`, los README, las síntesis de `references/`, `templates/`). Los textos oficiales de WIPO Lex reproducidos literalmente en `references/` y los dos PDF oficiales de la OMPI/CNIPA siguen siendo propiedad de sus organismos emisores: se adjuntan para facilitar la verificación y **no están cubiertos por esta licencia** — respete las condiciones de sus fuentes.

Toda conclusión producida con esta habilidad debe contrastarse con el derecho nacional de la Parte designada y con los hechos del caso antes de invocarla; como ayuda a la práctica, no constituye asesoramiento jurídico.

---

## Contacto

Mantenido por **Hui Ning IP (辉宁知识产权)** — equipo chino de agentes de patentes y marcas, con cobertura de tramitación de patentes, tramitación de marcas y servicios internacionales de propiedad intelectual.

- Las Issues son bienvenidas para informar de datos caducados, erratas de cita o problemas de script. **Al informar de una discrepancia en un dato volátil, adjunte la URL de la página oficial y una captura de pantalla**; la fecha de corte se actualizará tras verificarlo.
- Si conoce una posición práctica local en alguna Parte Contratante, compártala: esta habilidad es neutral por diseño, y esas diferencias de jurisdicción son precisamente lo que más necesita.
