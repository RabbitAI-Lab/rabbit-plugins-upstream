---
name: "context-compressor"
description: "Compresie ultra-densă și gestionare automată a contextului prin fișiere de stare (NCM) pentru menținerea continuității în sesiuni masive fără impact asupra latenței."
---

# context-compressor

## Description
Compresie ultra-densă și gestionare automată a contextului prin fișiere de stare (NCM) pentru menținerea continuității în sesiuni masive fără impact asupra latenței.

## Invocation
`context-compressor compress --target <file_path>`
`context-compressor load --source <file_path>`
`context-compressor auto --mode <monitor|prune>`

## Procedure

### compress
1. Analizează istoricul recent și datele din `<target>`.
2. Extrage informația esențială (Obiectiv, Status, Decizii, Knowledge, Next step).
3. Transformă în format NCM (Neural-Compressed Markdown) ultra-dens:
   - Tag-uri scurte: `[O]`, `[S]`, `[D]`, `[K]`, `[N]`.
   - Format: `[Tag]:valoare` sau `[Tag]:cheie:valoare`.
   - Elimină gramatica și zgomotul conversational.
4. Scrie în `<target>` și execută pruning pentru a menține fișierul la dimensiune minimă.

### load
1. Citește fișierul `<source>`.
2. Reconstruiește starea mentală a agentului prin procesarea tag-urilor.
3. Afișează un rezumat scurt pentru confirmare.

### auto (Background Mode)
1. **Monitorizare:** Verifică periodic numărul de tokeni al sesiunii active.
2. **Trigger:** La atingerea unui prag (ex: 50k tokeni), declanșează automat `compress` pe fișierul de stare al proiectului.
3. **Pruning:** Identifică și elimină informațiile redundante sau expirate din fișierele de stare pentru a preveni creșterea dimensiunii fișierelor.

## Bundled Resources
- `assets/templates/ncm_structure.json`: Schema de structură pentru tag-uri.

## Verification
- `compress`: Dimensiunea fișierului este < 5% din volumul de text original.
- `load`: Reconstrucția stării este 100% fidelă deciziilor extrase.
- `auto`: Monitorul detectează pragul și declanșează scrierea fără intervenție manuală.
