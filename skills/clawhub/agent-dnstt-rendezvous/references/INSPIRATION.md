# Inspiration, license boundaries, and originality

This skill is an original coordination layer. It contains no copied source
code, assets, branding, UI, profile URI, configuration format, or prose from
the projects below.

## Studied projects

### anonvector/dnstt

- URL: https://github.com/anonvector/dnstt
- License observed: AGPL-3.0
- High-level lesson: DNSTT separates a local TCP listener from a remote TCP
  service, authenticates the server by public key, and may use UDP/DoH/DoT DNS
  transports.
- Not copied: implementation, packages, command parser, protocol code,
  documentation, server hardening patches, or license text.

### anonvector/SlipNet

- URL: https://github.com/anonvector/SlipNet
- License observed: source-available with redistribution/derivative-product
  restrictions.
- High-level lesson: connection profiles, explicit transport selection,
  resolver health, and user-visible runtime state reduce configuration errors.
- Not copied: source, app design, branding, profile links/URIs, scanners,
  resolver lists, configuration schema, or text.

### anonvector/slipgate

- URL: https://github.com/anonvector/slipgate
- License observed: AGPL-3.0
- High-level lesson: server-side lifecycle, status, bounded services, and
  explicit client handoff are operationally important.
- Not copied: installer, service manager, CLI, share format, scripts, or code.

### anonvector/DNS-Multiplexer

- URL: https://github.com/anonvector/DNS-Multiplexer
- High-level lesson: cooperating components need clear health states and must
  avoid treating one resolver/path observation as universal.
- Not copied: multiplexer, scanner, embedded binaries, resolver logic, cache,
  SSH chain, or source.

### WhiteDNS/WhiteDNS-Android

- URL: https://github.com/WhiteDNS/WhiteDNS-Android
- License observed: WhiteDNS Source-Available Proprietary License; it prohibits
  redistribution, unofficial derivatives, rebranding, and competing products.
- High-level lesson: separate engine profiles, scoped runtime state, explicit
  resolver configuration, progress, and traffic status help operators.
- Not copied: any code, UI, assets, branding, Android design, native binaries,
  configuration/profile formats, or text. This skill is not a WhiteDNS fork or
  compatible app and does not use the WhiteDNS name in its product identity.

### WhiteDNS/CottenDNS

- URL: https://github.com/WhiteDNS/CottenDNS
- License observed: MIT with attribution to MasterDnsVPN, StormDNS, and
  CottenDNS contributors.
- High-level lesson: client/server roles, bounded presets, and explicit
  reliability diagnostics are useful in high-latency environments.
- Not copied: source code, protocol, config keys, presets, installers, or docs.

### Original DNSTT documentation

- URL: https://www.bamsoftware.com/software/dnstt/
- License statement observed: original dnstt is public domain.
- Used only to confirm public operational facts such as DNS NS delegation,
  public/private key roles, and conventional client/server flag shapes.

## New design created here

The following elements are original to this skill:

- `agent-dnstt-rendezvous/v1` short-lived card schema;
- card IDs over canonical JSON;
- optional coordination HMAC that is never stored in the card;
- mandatory out-of-band server public-key fingerprint pinning;
- authorization reference and explicit `--ack-authorized` gate;
- loopback-only defaults for upstream and client listener;
- deterministic JSON argv plans with no subprocess execution;
- public-key materialization plan without private-key transfer;
- secret-free agent status reports and state machine;
- bounded, read-only diagnostics with no resolver scanning;
- tests that enforce tamper detection, key permissions, loopback defaults, and
  non-execution.

## Attribution principle

Inspiration is credited, but this skill neither incorporates nor redistributes
any referenced project's code. If future contributors add third-party code,
they must perform a fresh license review, add required notices, identify exact
files/commits, and update the verification hash before publication.
