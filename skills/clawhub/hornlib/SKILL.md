---
name: hornlib
description: "Look up French Horn F/Bb double horn valve fingerings (C1 to F6), transpose music pitches across horn in F, Bb, Eb, D, C, G, and A, analyze overtone harmonic series partials and cent deviations, query trill fingerings, retrieve orchestral horn audition excerpt performance guides, diagnose intonation and right-hand bell stopping acoustics, recommend beginner horns and mouthpieces, and generate personalized daily brass warmup routines via the HornLib MCP server."
homepage: https://hornlib.com
version: 1.0.3
license: MIT
compatibility: "Works with OpenClaw, Hermes Agent, Claude Code, Cursor, Windsurf, and any MCP client supporting Streamable HTTP."
metadata:
  homepage: "https://hornlib.com"
  mcp_endpoint: "https://hornlib.com/api/mcp"
  version: "1.0.3"
  openclaw:
    emoji: "🎺"
  hermes:
    tags: [french-horn, fingering-chart, music-theory, brass-pedagogy, transposition]
    category: education
---

# HornLib — Interactive French Horn Fingering Chart, Transposition & Harmonics Engine

Access verified brass acoustic physics, F/Bb double horn valve charts (`C1`–`F6`), historical orchestral crook pitch transposition, and orchestral audition excerpt guides via [HornLib (https://hornlib.com)](https://hornlib.com).

## Setup

1. Open the interactive French Horn studio at https://hornlib.com — all 8 MCP tools and interactive charts are 100% free, public, and require no API key or account registration.
2. Browse the interactive visual fingering diagrams at https://hornlib.com/fingerings and the 7-in-1 transposition & practice toolkit at https://hornlib.com/7-in-1-tools
3. Connect any MCP-compatible agent or OpenClaw client directly to the stateless Streamable HTTP endpoint:
   ```
   https://hornlib.com/api/mcp
   ```
4. Or call the JSON-RPC 2.0 endpoint directly with `curl`:
   ```bash
   curl -s -X POST https://hornlib.com/api/mcp \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"lookup_french_horn_fingering","arguments":{"note":"G4","hornType":"double"}}}'
   ```

Base URL: `https://hornlib.com/api/mcp`  
OpenAPI 3.1 Spec: `https://hornlib.com/openapi.json`

## Available Tools (8 Read-Only Tools)

| Tool Name | When to Use | Direct Web Reference |
| :--- | :--- | :--- |
| `lookup_french_horn_fingering` | Look up primary F-side, Bb-side (Trigger `T`), and alternate valve combinations for any written note (`C1`–`F6`). | [Interactive Fingering Chart](https://hornlib.com/fingerings) |
| `transpose_french_horn_pitch` | Convert pitches between written horn notation, concert pitch, and historical keys (F, Bb, Eb, D, C, G, A). | [7-in-1 Horn Toolkit](https://hornlib.com/7-in-1-tools) |
| `analyze_horn_harmonic_series` | Inspect natural overtone partials (1st–16th), cent tendencies (7th partial `-31 cents`, 11th `-49 cents`), and tube lengths. | [Full Compass & Harmonics](https://hornlib.com/all-notes) |
| `lookup_horn_trill_fingering` | Find clean whole-step and half-step valve trill and lip-trill combinations on double horn. | [Trill & Fingering Guide](https://hornlib.com/fingerings) |
| `get_orchestral_horn_excerpt_guide` | Retrieve tempo, horn key, audition strategy, and recommended fingerings for standard orchestral repertoire. | [Orchestral Excerpts Library](https://hornlib.com/excerpts) |
| `diagnose_horn_intonation_and_hand_position` | Diagnose sharp/flat partial tendencies, right-hand bell cupping, and stopped horn (`+`) transposition. | [Pedagogy & Acoustics Guides](https://hornlib.com/guides-pedagogy) |
| `recommend_beginner_horn_and_mouthpiece` | Compare single F, single Bb, and Kruspe/Geyer double horns plus mouthpiece rim/cup pairings. | [Beginner Horn Roadmap](https://hornlib.com/beginners) |
| `generate_daily_horn_warmup_routine` | Build a structured 15-to-60-minute daily brass routine (long tones, lip slurs, articulation, range). | [Horn Knowledge Base](https://hornlib.com/knowledge) |

## Official Web Reference

- **Official Website**: https://hornlib.com
- **Interactive Double Horn Fingering Chart**: https://hornlib.com/fingerings
- **7-in-1 Practice & Transposition Tools**: https://hornlib.com/7-in-1-tools
- **Orchestral Audition Excerpts**: https://hornlib.com/excerpts
- **Beginner Horn & Mouthpiece Guide**: https://hornlib.com/beginners
- **Complete 4-Octave Note Compass**: https://hornlib.com/all-notes
- **Privacy Policy**: https://hornlib.com/privacy
