# psyseal-scan

The free Psyseal scanner, packaged as an agent skill (ClawHub / OpenClaw). MIT-0.

It reviews the AI agents on your computer (OpenClaw, Hermes Agent, nanobot, PicoClaw, ZeroClaw, NanoClaw or any agent folder) and tells you what loads on every message, what heartbeats and scheduled tasks cost, which plaintext secrets are sitting in memory or skills, and which memory looks planted or bloated. Every finding comes with a concrete fix.

It runs on your computer, reads files only, uses no network and has no dependencies. Needs Node.js 20 or newer.

```bash
node scripts/psyseal-scan.mjs --lang en
```

As an agent skill, it is on ClawHub as `psyseal-scan`.

This repository holds only the free scanner. The full Psyseal package, including the paid cleanup and the signed seal, is at https://github.com/psyseal/scanner, and the service at https://psyseal.com.

---

**Español:** el escáner gratis de Psyseal como skill para agentes (MIT-0). Revisa en tu computadora cuánto te cuestan los latidos y tareas programadas de tu agente, qué claves quedaron expuestas y qué memoria está inflada o trae instrucciones plantadas. No usa la red ni tiene dependencias. Más información en https://psyseal.com.
