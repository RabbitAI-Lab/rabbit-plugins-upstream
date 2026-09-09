# Process → Equipment Mapping Library · Semiconductor & Optoelectronics (seed v0.1, 2026-09-09)

Row shape: EIA signal → equipment class (vocabulary layer) → tier signal → representative vendors (domestic / imported) → reading rationale.

Usage discipline:
- The vendor column reflects industry-common-knowledge mappings, for lead generation only — it is NOT a judgment about any specific company's equipment sourcing. That judgment must return to the EIA equipment-source column and external evidence
- Rows marked 【to verify】 must never be cited as conclusions; they are screening directions only
- Append rows after every engagement; write nothing without evidence; gas separation and other tracks get their own files

| EIA signal (process / keyword) | Equipment class | Tier signal | Representative vendors (CN / imported) | Reading rationale |
|---|---|---|---|---|
| RCA cleaning, batch cleaning | Wet bench (batch) | manual / semi-auto / auto; megasonic | ACM Research (SACMI), UCT / DNS, TEL | front-end cleaning standard |
| Single-wafer cleaning, SPM | Single-wafer wet cleaner | 300mm capability, chamber count | SACMI, ACM Research; Kingsemi / DNS, SEMES | single-wafer = more advanced signal |
| Oxidation / diffusion / annealing (furnace) | Vertical furnace | temperature zones, wafer capacity | NAURA / TEL | — |
| Lithography, exposure | Lithography scanner | i-line / KrF / ArF wavelength | SMEE / ASML, Nikon | wavelength = core generation signal |
| Coat, develop | Track (coat & develop) | coupled with scanner | Kingsemi / TEL | — |
| Plasma etch, dry etch | Etcher (CCP/ICP) | chamber count, dielectric / conductor | AMEC, NAURA / LAM, AMAT, TEL | — |
| Sputtering, evaporation, vacuum coating | PVD / evaporator | target count, vacuum level | NAURA / AMAT, Ulvac | same family as IR VOx sputtering; "vacuum coater" normalizes here |
| CVD / PECVD / LPCVD | CVD tool | deposited films (SiN / SiO / poly) | Piotech / AMAT, LAM, TEL | — |
| Epitaxy (T2SL / GaSb / InAs) | MBE system | chambers, wafers per platen | 【to verify】 / Veeco, Riber | core tool for T2SL IR detectors |
| Epitaxy (GaN / LED / power) | MOCVD | chambers, wafers per chamber | AMEC; others 【to verify】 / Aixtron, Veeco | — |
| Ion implantation | Implanter | energy class, beam current | Wanye (KST), CETC-48 line / Axcelis, AMAT | — |
| CMP | Polisher | head count, 300mm | Hwatsing / AMAT, Ebara | — |
| Metrology, inspection, AOI | Metrology / inspection | optical / e-beam | Skyverse, Accotest, Raysolve / KLA, Onto | — |
| Dicing, cutting | Dicer | lane count | Lightforce 【to verify】 / DISCO | assembly segment |
| Wire bond, flip-chip, indium bump interconnect | Bonder | Au / Cu wire, flip-chip | Xinyichang / ASMPT, K&S | same family as IR flip-chip interconnect |
| Wafer-level bonding, vacuum packaging, WL-CSP | Wafer-level packaging | anodic / eutectic / frit, vacuum chamber | 【to verify】 / SUSS, EVG | wafer-level vs. ceramic package = cost-structure watershed |
| Mold, encapsulation | Molding equipment | — | 【to verify】 / TOWA | — |
| Nanoimprint, UV imprint | Imprint lithography | area, resolution, soft / hard stamp | in-house common / EVG, SUSS, Obducat, Canon | NIL has a high in-house rate; verify "in-house" against the equipment-source column |
| Cooled-detector accessories (Stirling / JT) | Micro cryocooler / dewar | cooling power, lifetime | 【to verify】 / Ricor, AIM | cooler buy vs. build is a key cost driver |
| Specialty gases (silane / phosphine / arsine) | Gas cabinet / cylinder farm | — | — | gas species = epitaxy / implant fingerprint, used for reverse inference |
| Hydrofluoric acid, wet etch | Wet etch bench | — | — | HF present → a wet-etch step exists |

## Track coverage status

- Built: semiconductor front-end / assembly, IR detectors (T2SL/VOx key rows merged above), nanoimprint
- To build (create files as engagements require): gas separation (membrane / PSA), AR optics, others
