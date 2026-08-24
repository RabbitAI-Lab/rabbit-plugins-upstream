#!/usr/bin/env node
/**
 * Ava OpenClaw CLI — thin HTTP client over Ava MCP + REST.
 * Zero dependencies (Node 20+ fetch). Testnet is the default mode.
 *
 * Usage:
 *   node scripts/ava.mjs session
 *   node scripts/ava.mjs tools
 *   node scripts/ava.mjs turn "Swap 10 USDC to SUI on sui with 50 bps slip"
 *   node scripts/ava.mjs approve <executionId>
 *   node scripts/ava.mjs portfolio
 *   node scripts/ava.mjs price SUI
 *   node scripts/ava.mjs call ava_get_price '{"asset":"SUI"}'
 *   node scripts/ava.mjs credential --key-file ~/.config/ava-openclaw/signer.key
 *
 * `credential` obtains a short-lived (15 minute) execute-scoped credential by
 * signing Ava's EIP-712 principal challenge with the same key your mandates
 * are signed with, then sends it automatically as x-ava-agent-credential on
 * every later authenticated call. Required for identity-gated execute paths;
 * a mandate must already be signed with this key (mandateSignerFor refuses
 * unknown signers server-side: POST /v1/principals/challenge 409s with
 * PRINCIPAL_SIGNER_UNKNOWN otherwise). The raw key is never accepted as a CLI
 * argument: pass --key-file <path> or --key-env <ENV_VAR_NAME>, never
 * --key <hex> (argv is visible to every other process on the machine).
 */

import { readFileSync, writeFileSync, mkdirSync, existsSync } from "node:fs";
import { homedir, hostname } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const STATE_DIR = join(homedir(), ".config", "ava-openclaw");
const STATE_FILE = join(STATE_DIR, "state.json");

function env(name, fallback = "") {
  const v = process.env[name];
  return v !== undefined && v.trim().length > 0 ? v.trim() : fallback;
}

function loadState() {
  try {
    if (!existsSync(STATE_FILE)) return {};
    return JSON.parse(readFileSync(STATE_FILE, "utf8"));
  } catch {
    return {};
  }
}

function saveState(partial) {
  mkdirSync(STATE_DIR, { recursive: true });
  const next = { ...loadState(), ...partial, updatedAt: new Date().toISOString() };
  writeFileSync(STATE_FILE, JSON.stringify(next, null, 2), { mode: 0o600 });
  return next;
}

function baseUrl() {
  return env("AVA_API_BASE", "http://127.0.0.1:8787").replace(/\/$/, "");
}

function portal() {
  return env("AVA_PORTAL", loadState().portal ?? "sui").toLowerCase();
}

function userId() {
  return env("AVA_USER_ID", loadState().userId ?? "");
}

/**
 * The bearer credential. The user id names an account; this proves we hold it.
 * Ava derives the caller from this token server-side, so a userId passed in a
 * tool argument can only ever agree with it, never widen it.
 */
function token() {
  return env("AVA_TOKEN", loadState().token ?? "");
}

/**
 * The scoped execute credential minted by `credential`. Sent alongside the
 * bearer token, never instead of it: the token says who is asking, this says
 * which agent instance is asking and under what scope. Absence is not an
 * error here — routes that check it treat a missing header as "no credential
 * presented" and refuse by name; routes that don't check it ignore it.
 */
function credentialSecret() {
  return env("AVA_AGENT_CREDENTIAL", loadState().credential ?? "");
}

function requireUserId() {
  const id = userId();
  if (!id) {
    fail(
      "AVA_USER_ID missing. Run: node scripts/ava.mjs session\nOr export AVA_USER_ID=usr_...",
    );
  }
  return id;
}

function requireToken() {
  const value = token();
  if (!value) {
    fail(
      "No Ava session token. Run: node scripts/ava.mjs session\nOr export AVA_TOKEN=ava_st_...\nA user id on its own is not a credential and the API will refuse it.",
    );
  }
  return value;
}

function fail(msg, code = 1) {
  console.error(msg);
  process.exit(code);
}

// ── EIP-712 signing: hex/byte helpers ────────────────────────────────────

function bytesToHex(bytes) {
  return `0x${Array.from(bytes, (b) => b.toString(16).padStart(2, "0")).join("")}`;
}

function hexToBytes(hex) {
  const clean = hex.startsWith("0x") || hex.startsWith("0X") ? hex.slice(2) : hex;
  if (clean.length % 2 !== 0 || /[^0-9a-fA-F]/u.test(clean)) {
    throw new Error(`Not a hex string: ${hex}`);
  }
  const out = new Uint8Array(clean.length / 2);
  for (let i = 0; i < out.length; i += 1) {
    out[i] = Number.parseInt(clean.slice(i * 2, i * 2 + 2), 16);
  }
  return out;
}

function concatBytes(...arrays) {
  const total = arrays.reduce((n, a) => n + a.length, 0);
  const out = new Uint8Array(total);
  let offset = 0;
  for (const a of arrays) {
    out.set(a, offset);
    offset += a.length;
  }
  return out;
}

function padTo32(value) {
  let remaining = typeof value === "bigint" ? value : BigInt(value);
  if (remaining < 0n) {
    throw new Error("This EIP-712 encoder does not support negative integers.");
  }
  const out = new Uint8Array(32);
  for (let i = 31; i >= 0 && remaining > 0n; i -= 1) {
    out[i] = Number(remaining & 0xffn);
    remaining >>= 8n;
  }
  return out;
}

/**
 * Read a signing private key from a FILE or an ENV VAR — never from argv.
 *
 * argv is visible in `ps`, `/proc/<pid>/cmdline`, and shell history on every
 * multi-user or logged machine. A --key flag that took the raw hex would leak
 * the one key that signs this principal's mandates the first time anyone ran
 * `ps aux` while the command was in flight, so that flag does not exist here:
 * `cmdCredential` refuses it explicitly before this function is ever reached.
 */
function readPrivateKey({ keyFile, keyEnvName }) {
  let raw;
  let source;
  if (keyFile) {
    source = `key file ${keyFile}`;
    try {
      raw = readFileSync(keyFile, "utf8");
    } catch (e) {
      fail(`Could not read ${source}: ${e.message}`);
    }
  } else {
    source = `env var ${keyEnvName}`;
    raw = process.env[keyEnvName];
    if (raw === undefined) {
      fail(
        `${source} is not set. It must hold the hex private key that signs your mandates; ` +
          "the credential command reads it from a file or an env var, never from argv.",
      );
    }
  }
  const clean = raw.trim().replace(/^0x/iu, "");
  if (!/^[0-9a-fA-F]{64}$/u.test(clean)) {
    fail(
      `${source} does not hold a 32-byte secp256k1 private key (64 hex chars, optional 0x prefix). ` +
        "Refusing to sign a credential challenge with something that is not a private key.",
    );
  }
  return hexToBytes(clean);
}

/**
 * secp256k1 + keccak256, vendored (not installed) so this package stays the
 * zero-dependency CLI its own header promises: a `credential` subcommand that
 * quietly required `pnpm install` at the monorepo root to gain a new
 * dependency would break the "one-command" premise this whole subcommand
 * exists to satisfy.
 *
 * This is a real, unmodified build of @noble/curves (secp256k1) and
 * @noble/hashes (keccak_256) — the same MIT-licensed, audited libraries
 * `packages/tenancy/src/principal-challenge.ts` (the server-side verifier
 * this signs for) already depends on — bundled with esbuild into one
 * self-contained ES module and loaded from a data: URL. No hand-rolled
 * elliptic-curve math lives in this file.
 *
 * Regenerate with (from the repo root, after `pnpm install`):
 *   printf 'export { secp256k1 } from "@noble/curves/secp256k1";\nexport { keccak_256 } from "@noble/hashes/sha3";\n' > /tmp/noble-entry.mjs
 *   ./node_modules/.bin/esbuild /tmp/noble-entry.mjs --bundle --format=esm \
 *     --platform=node --target=node20 --minify --outfile=/tmp/noble-bundle.mjs
 * then paste `JSON.stringify(readFileSync("/tmp/noble-bundle.mjs", "utf8"))`
 * as VENDORED_NOBLE_SOURCE below. @noble/curves 1.9.0, @noble/hashes 1.7.1 —
 * the exact versions apps/api-worker and packages/tenancy pin today.
 */
const VENDORED_NOBLE_SOURCE = "import*as z from\"node:crypto\";var ct=z&&typeof z==\"object\"&&\"webcrypto\"in z?z.webcrypto:z&&typeof z==\"object\"&&\"randomBytes\"in z?z:void 0;function ft(t){return t instanceof Uint8Array||ArrayBuffer.isView(t)&&t.constructor.name===\"Uint8Array\"}function Et(t){if(!Number.isSafeInteger(t)||t<0)throw new Error(\"positive integer expected, got \"+t)}function G(t,...e){if(!ft(t))throw new Error(\"Uint8Array expected\");if(e.length>0&&!e.includes(t.length))throw new Error(\"Uint8Array expected of length \"+e+\", got length=\"+t.length)}function Tt(t){if(typeof t!=\"function\"||typeof t.create!=\"function\")throw new Error(\"Hash should be wrapped by utils.createHasher\");Et(t.outputLen),Et(t.blockLen)}function pt(t,e=!0){if(t.destroyed)throw new Error(\"Hash instance has been destroyed\");if(e&&t.finished)throw new Error(\"Hash#digest() has already been called\")}function Ee(t,e){G(t);let r=e.outputLen;if(t.length<r)throw new Error(\"digestInto() expects output buffer of length at least \"+r)}function at(...t){for(let e=0;e<t.length;e++)t[e].fill(0)}function Rt(t){return new DataView(t.buffer,t.byteOffset,t.byteLength)}function X(t,e){return t<<32-e|t>>>e}var ve=typeof Uint8Array.from([]).toHex==\"function\"&&typeof Uint8Array.fromHex==\"function\",Bn=Array.from({length:256},(t,e)=>e.toString(16).padStart(2,\"0\"));function W(t){if(G(t),ve)return t.toHex();let e=\"\";for(let r=0;r<t.length;r++)e+=Bn[t[r]];return e}var P={_0:48,_9:57,A:65,F:70,a:97,f:102};function Be(t){if(t>=P._0&&t<=P._9)return t-P._0;if(t>=P.A&&t<=P.F)return t-(P.A-10);if(t>=P.a&&t<=P.f)return t-(P.a-10)}function ut(t){if(typeof t!=\"string\")throw new Error(\"hex string expected, got \"+typeof t);if(ve)return Uint8Array.fromHex(t);let e=t.length,r=e/2;if(e%2)throw new Error(\"hex string expected, got unpadded hex of length \"+e);let n=new Uint8Array(r);for(let o=0,i=0;o<r;o++,i+=2){let s=Be(t.charCodeAt(i)),c=Be(t.charCodeAt(i+1));if(s===void 0||c===void 0){let f=t[i]+t[i+1];throw new Error('hex string expected, got non-hex character \"'+f+'\" at index '+i)}n[o]=s*16+c}return n}function Se(t){if(typeof t!=\"string\")throw new Error(\"string expected\");return new Uint8Array(new TextEncoder().encode(t))}function vt(t){return typeof t==\"string\"&&(t=Se(t)),G(t),t}function Y(...t){let e=0;for(let n=0;n<t.length;n++){let o=t[n];G(o),e+=o.length}let r=new Uint8Array(e);for(let n=0,o=0;n<t.length;n++){let i=t[n];r.set(i,o),o+=i.length}return r}var xt=class{};function Ae(t){let e=n=>t().update(vt(n)).digest(),r=t();return e.outputLen=r.outputLen,e.blockLen=r.blockLen,e.create=()=>t(),e}function qt(t=32){if(ct&&typeof ct.getRandomValues==\"function\")return ct.getRandomValues(new Uint8Array(t));if(ct&&typeof ct.randomBytes==\"function\")return Uint8Array.from(ct.randomBytes(t));throw new Error(\"crypto.getRandomValues must be defined\")}function En(t,e,r,n){if(typeof t.setBigUint64==\"function\")return t.setBigUint64(e,r,n);let o=BigInt(32),i=BigInt(4294967295),s=Number(r>>o&i),c=Number(r&i),f=n?4:0,b=n?0:4;t.setUint32(e+f,s,n),t.setUint32(e+b,c,n)}function _e(t,e,r){return t&e^~t&r}function Ie(t,e,r){return t&e^t&r^e&r}var Nt=class extends xt{constructor(e,r,n,o){super(),this.finished=!1,this.length=0,this.pos=0,this.destroyed=!1,this.blockLen=e,this.outputLen=r,this.padOffset=n,this.isLE=o,this.buffer=new Uint8Array(e),this.view=Rt(this.buffer)}update(e){pt(this),e=vt(e),G(e);let{view:r,buffer:n,blockLen:o}=this,i=e.length;for(let s=0;s<i;){let c=Math.min(o-this.pos,i-s);if(c===o){let f=Rt(e);for(;o<=i-s;s+=o)this.process(f,s);continue}n.set(e.subarray(s,s+c),this.pos),this.pos+=c,s+=c,this.pos===o&&(this.process(r,0),this.pos=0)}return this.length+=e.length,this.roundClean(),this}digestInto(e){pt(this),Ee(e,this),this.finished=!0;let{buffer:r,view:n,blockLen:o,isLE:i}=this,{pos:s}=this;r[s++]=128,at(this.buffer.subarray(s)),this.padOffset>o-s&&(this.process(n,0),s=0);for(let g=s;g<o;g++)r[g]=0;En(n,o-8,BigInt(this.length*8),i),this.process(n,0);let c=Rt(e),f=this.outputLen;if(f%4)throw new Error(\"_sha2: outputLen should be aligned to 32bit\");let b=f/4,x=this.get();if(b>x.length)throw new Error(\"_sha2: outputLen bigger than state\");for(let g=0;g<b;g++)c.setUint32(4*g,x[g],i)}digest(){let{buffer:e,outputLen:r}=this;this.digestInto(e);let n=e.slice(0,r);return this.destroy(),n}_cloneInto(e){e||(e=new this.constructor),e.set(...this.get());let{blockLen:r,buffer:n,length:o,finished:i,destroyed:s,pos:c}=this;return e.destroyed=s,e.finished=i,e.length=o,e.pos=c,o%r&&e.buffer.set(n),e}clone(){return this._cloneInto()}},$=Uint32Array.from([1779033703,3144134277,1013904242,2773480762,1359893119,2600822924,528734635,1541459225]);var vn=Uint32Array.from([1116352408,1899447441,3049323471,3921009573,961987163,1508970993,2453635748,2870763221,3624381080,310598401,607225278,1426881987,1925078388,2162078206,2614888103,3248222580,3835390401,4022224774,264347078,604807628,770255983,1249150122,1555081692,1996064986,2554220882,2821834349,2952996808,3210313671,3336571891,3584528711,113926993,338241895,666307205,773529912,1294757372,1396182291,1695183700,1986661051,2177026350,2456956037,2730485921,2820302411,3259730800,3345764771,3516065817,3600352804,4094571909,275423344,430227734,506948616,659060556,883997877,958139571,1322822218,1537002063,1747873779,1955562222,2024104815,2227730452,2361852424,2428436474,2756734187,3204031479,3329325298]),tt=new Uint32Array(64),Wt=class extends Nt{constructor(e=32){super(64,e,8,!1),this.A=$[0]|0,this.B=$[1]|0,this.C=$[2]|0,this.D=$[3]|0,this.E=$[4]|0,this.F=$[5]|0,this.G=$[6]|0,this.H=$[7]|0}get(){let{A:e,B:r,C:n,D:o,E:i,F:s,G:c,H:f}=this;return[e,r,n,o,i,s,c,f]}set(e,r,n,o,i,s,c,f){this.A=e|0,this.B=r|0,this.C=n|0,this.D=o|0,this.E=i|0,this.F=s|0,this.G=c|0,this.H=f|0}process(e,r){for(let g=0;g<16;g++,r+=4)tt[g]=e.getUint32(r,!1);for(let g=16;g<64;g++){let a=tt[g-15],l=tt[g-2],w=X(a,7)^X(a,18)^a>>>3,E=X(l,17)^X(l,19)^l>>>10;tt[g]=E+tt[g-7]+w+tt[g-16]|0}let{A:n,B:o,C:i,D:s,E:c,F:f,G:b,H:x}=this;for(let g=0;g<64;g++){let a=X(c,6)^X(c,11)^X(c,25),l=x+a+_e(c,f,b)+vn[g]+tt[g]|0,E=(X(n,2)^X(n,13)^X(n,22))+Ie(n,o,i)|0;x=b,b=f,f=c,c=s+l|0,s=i,i=o,o=n,n=l+E|0}n=n+this.A|0,o=o+this.B|0,i=i+this.C|0,s=s+this.D|0,c=c+this.E|0,f=f+this.F|0,b=b+this.G|0,x=x+this.H|0,this.set(n,o,i,s,c,f,b,x)}roundClean(){at(tt)}destroy(){this.set(0,0,0,0,0,0,0,0),at(this.buffer)}};var He=Ae(()=>new Wt);var Ct=class extends xt{constructor(e,r){super(),this.finished=!1,this.destroyed=!1,Tt(e);let n=vt(r);if(this.iHash=e.create(),typeof this.iHash.update!=\"function\")throw new Error(\"Expected instance of class which extends utils.Hash\");this.blockLen=this.iHash.blockLen,this.outputLen=this.iHash.outputLen;let o=this.blockLen,i=new Uint8Array(o);i.set(n.length>o?e.create().update(n).digest():n);for(let s=0;s<i.length;s++)i[s]^=54;this.iHash.update(i),this.oHash=e.create();for(let s=0;s<i.length;s++)i[s]^=106;this.oHash.update(i),at(i)}update(e){return pt(this),this.iHash.update(e),this}digestInto(e){pt(this),G(e,this.outputLen),this.finished=!0,this.iHash.digestInto(e),this.oHash.update(e),this.oHash.digestInto(e),this.destroy()}digest(){let e=new Uint8Array(this.oHash.outputLen);return this.digestInto(e),e}_cloneInto(e){e||(e=Object.create(Object.getPrototypeOf(this),{}));let{oHash:r,iHash:n,finished:o,destroyed:i,blockLen:s,outputLen:c}=this;return e=e,e.finished=o,e.destroyed=i,e.blockLen=s,e.outputLen=c,e.oHash=r._cloneInto(e.oHash),e.iHash=n._cloneInto(e.iHash),e}clone(){return this._cloneInto()}destroy(){this.destroyed=!0,this.oHash.destroy(),this.iHash.destroy()}},$t=(t,e,r)=>new Ct(t,e).update(r).digest();$t.create=(t,e)=>new Ct(t,e);var Ft=BigInt(0),Jt=BigInt(1);function St(t,e=\"\"){if(typeof t!=\"boolean\"){let r=e&&`\"${e}\"`;throw new Error(r+\"expected boolean, got type=\"+typeof t)}return t}function et(t,e,r=\"\"){let n=ft(t),o=t?.length,i=e!==void 0;if(!n||i&&o!==e){let s=r&&`\"${r}\" `,c=i?` of length ${e}`:\"\",f=n?`length=${o}`:`type=${typeof t}`;throw new Error(s+\"expected Uint8Array\"+c+\", got \"+f)}return t}function At(t){let e=t.toString(16);return e.length&1?\"0\"+e:e}function Le(t){if(typeof t!=\"string\")throw new Error(\"hex string expected, got \"+typeof t);return t===\"\"?Ft:BigInt(\"0x\"+t)}function gt(t){return Le(W(t))}function te(t){return G(t),Le(W(Uint8Array.from(t).reverse()))}function Vt(t,e){return ut(t.toString(16).padStart(e*2,\"0\"))}function ee(t,e){return Vt(t,e).reverse()}function V(t,e,r){let n;if(typeof e==\"string\")try{n=ut(e)}catch(i){throw new Error(t+\" must be hex string or Uint8Array, cause: \"+i)}else if(ft(e))n=Uint8Array.from(e);else throw new Error(t+\" must be hex string or Uint8Array\");let o=n.length;if(typeof r==\"number\"&&o!==r)throw new Error(t+\" of length \"+r+\" expected, got \"+o);return n}var Qt=t=>typeof t==\"bigint\"&&Ft<=t;function Oe(t,e,r){return Qt(t)&&Qt(e)&&Qt(r)&&e<=t&&t<r}function Ue(t,e,r,n){if(!Oe(e,r,n))throw new Error(\"expected valid \"+t+\": \"+r+\" <= n < \"+n+\", got \"+e)}function Dt(t){let e;for(e=0;t>Ft;t>>=Jt,e+=1);return e}var nt=t=>(Jt<<BigInt(t))-Jt;function ke(t,e,r){if(typeof t!=\"number\"||t<2)throw new Error(\"hashLen must be a number\");if(typeof e!=\"number\"||e<2)throw new Error(\"qByteLen must be a number\");if(typeof r!=\"function\")throw new Error(\"hmacFn must be a function\");let n=l=>new Uint8Array(l),o=l=>Uint8Array.of(l),i=n(t),s=n(t),c=0,f=()=>{i.fill(1),s.fill(0),c=0},b=(...l)=>r(s,i,...l),x=(l=n(0))=>{s=b(o(0),l),i=b(),l.length!==0&&(s=b(o(1),l),i=b())},g=()=>{if(c++>=1e3)throw new Error(\"drbg: tried 1000 values\");let l=0,w=[];for(;l<e;){i=b();let E=i.slice();w.push(E),l+=i.length}return Y(...w)};return(l,w)=>{f(),x(l);let E;for(;!(E=w(g()));)x();return f(),E}}function _t(t,e,r={}){if(!t||typeof t!=\"object\")throw new Error(\"expected valid options object\");function n(o,i,s){let c=t[o];if(s&&c===void 0)return;let f=typeof c;if(f!==i||c===null)throw new Error(`param \"${o}\" is invalid: expected ${i}, got ${f}`)}Object.entries(e).forEach(([o,i])=>n(o,i,!1)),Object.entries(r).forEach(([o,i])=>n(o,i,!0))}function ne(t){let e=new WeakMap;return(r,...n)=>{let o=e.get(r);if(o!==void 0)return o;let i=t(r,...n);return e.set(r,i),i}}var Z=BigInt(0),D=BigInt(1),lt=BigInt(2),qe=BigInt(3),Ne=BigInt(4),Ce=BigInt(5),Sn=BigInt(7),Ve=BigInt(8),An=BigInt(9),De=BigInt(16);function K(t,e){let r=t%e;return r>=Z?r:e+r}function M(t,e,r){let n=t;for(;e-- >Z;)n*=n,n%=r;return n}function Te(t,e){if(t===Z)throw new Error(\"invert: expected non-zero number\");if(e<=Z)throw new Error(\"invert: expected positive modulus, got \"+e);let r=K(t,e),n=e,o=Z,i=D,s=D,c=Z;for(;r!==Z;){let b=n/r,x=n%r,g=o-s*b,a=i-c*b;n=r,r=x,o=s,i=c,s=g,c=a}if(n!==D)throw new Error(\"invert: does not exist\");return K(o,e)}function re(t,e,r){if(!t.eql(t.sqr(e),r))throw new Error(\"Cannot find square root\")}function Ze(t,e){let r=(t.ORDER+D)/Ne,n=t.pow(e,r);return re(t,n,e),n}function _n(t,e){let r=(t.ORDER-Ce)/Ve,n=t.mul(e,lt),o=t.pow(n,r),i=t.mul(e,o),s=t.mul(t.mul(i,lt),o),c=t.mul(i,t.sub(s,t.ONE));return re(t,c,e),c}function In(t){let e=rt(t),r=je(t),n=r(e,e.neg(e.ONE)),o=r(e,n),i=r(e,e.neg(n)),s=(t+Sn)/De;return(c,f)=>{let b=c.pow(f,s),x=c.mul(b,n),g=c.mul(b,o),a=c.mul(b,i),l=c.eql(c.sqr(x),f),w=c.eql(c.sqr(g),f);b=c.cmov(b,x,l),x=c.cmov(a,g,w);let E=c.eql(c.sqr(x),f),L=c.cmov(b,x,E);return re(c,L,f),L}}function je(t){if(t<qe)throw new Error(\"sqrt is not defined for small field\");let e=t-D,r=0;for(;e%lt===Z;)e/=lt,r++;let n=lt,o=rt(t);for(;Re(o,n)===1;)if(n++>1e3)throw new Error(\"Cannot find square root: probably non-prime P\");if(r===1)return Ze;let i=o.pow(n,e),s=(e+D)/lt;return function(f,b){if(f.is0(b))return b;if(Re(f,b)!==1)throw new Error(\"Cannot find square root\");let x=r,g=f.mul(f.ONE,i),a=f.pow(b,e),l=f.pow(b,s);for(;!f.eql(a,f.ONE);){if(f.is0(a))return f.ZERO;let w=1,E=f.sqr(a);for(;!f.eql(E,f.ONE);)if(w++,E=f.sqr(E),w===x)throw new Error(\"Cannot find square root\");let L=D<<BigInt(x-w-1),T=f.pow(g,L);x=w,g=f.sqr(T),a=f.mul(a,g),l=f.mul(l,T)}return l}}function Hn(t){return t%Ne===qe?Ze:t%Ve===Ce?_n:t%De===An?In(t):je(t)}var Ln=[\"create\",\"isValid\",\"is0\",\"neg\",\"inv\",\"sqrt\",\"sqr\",\"eql\",\"add\",\"sub\",\"mul\",\"pow\",\"div\",\"addN\",\"subN\",\"mulN\",\"sqrN\"];function oe(t){let e={ORDER:\"bigint\",MASK:\"bigint\",BYTES:\"number\",BITS:\"number\"},r=Ln.reduce((n,o)=>(n[o]=\"function\",n),e);return _t(t,r),t}function On(t,e,r){if(r<Z)throw new Error(\"invalid exponent, negatives unsupported\");if(r===Z)return t.ONE;if(r===D)return e;let n=t.ONE,o=e;for(;r>Z;)r&D&&(n=t.mul(n,o)),o=t.sqr(o),r>>=D;return n}function Zt(t,e,r=!1){let n=new Array(e.length).fill(r?t.ZERO:void 0),o=e.reduce((s,c,f)=>t.is0(c)?s:(n[f]=s,t.mul(s,c)),t.ONE),i=t.inv(o);return e.reduceRight((s,c,f)=>t.is0(c)?s:(n[f]=t.mul(s,n[f]),t.mul(s,c)),i),n}function Re(t,e){let r=(t.ORDER-D)/lt,n=t.pow(e,r),o=t.eql(n,t.ONE),i=t.eql(n,t.ZERO),s=t.eql(n,t.neg(t.ONE));if(!o&&!i&&!s)throw new Error(\"invalid Legendre symbol result\");return o?1:i?0:-1}function jt(t,e){e!==void 0&&Et(e);let r=e!==void 0?e:t.toString(2).length,n=Math.ceil(r/8);return{nBitLength:r,nByteLength:n}}function rt(t,e,r=!1,n={}){if(t<=Z)throw new Error(\"invalid field: expected ORDER > 0, got \"+t);let o,i,s=!1,c;if(typeof e==\"object\"&&e!=null){if(n.sqrt||r)throw new Error(\"cannot specify opts in two arguments\");let a=e;a.BITS&&(o=a.BITS),a.sqrt&&(i=a.sqrt),typeof a.isLE==\"boolean\"&&(r=a.isLE),typeof a.modFromBytes==\"boolean\"&&(s=a.modFromBytes),c=a.allowedLengths}else typeof e==\"number\"&&(o=e),n.sqrt&&(i=n.sqrt);let{nBitLength:f,nByteLength:b}=jt(t,o);if(b>2048)throw new Error(\"invalid field: expected ORDER of <= 2048 bytes\");let x,g=Object.freeze({ORDER:t,isLE:r,BITS:f,BYTES:b,MASK:nt(f),ZERO:Z,ONE:D,allowedLengths:c,create:a=>K(a,t),isValid:a=>{if(typeof a!=\"bigint\")throw new Error(\"invalid field element: expected bigint, got \"+typeof a);return Z<=a&&a<t},is0:a=>a===Z,isValidNot0:a=>!g.is0(a)&&g.isValid(a),isOdd:a=>(a&D)===D,neg:a=>K(-a,t),eql:(a,l)=>a===l,sqr:a=>K(a*a,t),add:(a,l)=>K(a+l,t),sub:(a,l)=>K(a-l,t),mul:(a,l)=>K(a*l,t),pow:(a,l)=>On(g,a,l),div:(a,l)=>K(a*Te(l,t),t),sqrN:a=>a*a,addN:(a,l)=>a+l,subN:(a,l)=>a-l,mulN:(a,l)=>a*l,inv:a=>Te(a,t),sqrt:i||(a=>(x||(x=Hn(t)),x(g,a))),toBytes:a=>r?ee(a,b):Vt(a,b),fromBytes:(a,l=!0)=>{if(c){if(!c.includes(a.length)||a.length>b)throw new Error(\"Field.fromBytes: expected \"+c+\" bytes, got \"+a.length);let E=new Uint8Array(b);E.set(a,r?0:E.length-a.length),a=E}if(a.length!==b)throw new Error(\"Field.fromBytes: expected \"+b+\" bytes, got \"+a.length);let w=r?te(a):gt(a);if(s&&(w=K(w,t)),!l&&!g.isValid(w))throw new Error(\"invalid field element: outside of range 0..ORDER\");return w},invertBatch:a=>Zt(g,a),cmov:(a,l,w)=>w?l:a});return Object.freeze(g)}function Me(t){if(typeof t!=\"bigint\")throw new Error(\"field order must be bigint\");let e=t.toString(2).length;return Math.ceil(e/8)}function se(t){let e=Me(t);return e+Math.ceil(e/2)}function ie(t,e,r=!1){let n=t.length,o=Me(e),i=se(e);if(n<16||n<i||n>1024)throw new Error(\"expected \"+i+\"-1024 bytes of input, got \"+n);let s=r?te(t):gt(t),c=K(s,e-D)+D;return r?ee(c,o):Vt(c,o)}var yt=BigInt(0),dt=BigInt(1);function It(t,e){let r=e.negate();return t?r:e}function Kt(t,e){let r=Zt(t.Fp,e.map(n=>n.Z));return e.map((n,o)=>t.fromAffine(n.toAffine(r[o])))}function Ye(t,e){if(!Number.isSafeInteger(t)||t<=0||t>e)throw new Error(\"invalid window size, expected [1..\"+e+\"], got W=\"+t)}function ce(t,e){Ye(t,e);let r=Math.ceil(e/t)+1,n=2**(t-1),o=2**t,i=nt(t),s=BigInt(t);return{windows:r,windowSize:n,mask:i,maxNumber:o,shiftBy:s}}function Ke(t,e,r){let{windowSize:n,mask:o,maxNumber:i,shiftBy:s}=r,c=Number(t&o),f=t>>s;c>n&&(c-=i,f+=dt);let b=e*n,x=b+Math.abs(c)-1,g=c===0,a=c<0,l=e%2!==0;return{nextN:f,offset:x,isZero:g,isNeg:a,isNegF:l,offsetF:b}}function Un(t,e){if(!Array.isArray(t))throw new Error(\"array expected\");t.forEach((r,n)=>{if(!(r instanceof e))throw new Error(\"invalid point at index \"+n)})}function kn(t,e){if(!Array.isArray(t))throw new Error(\"array of scalars expected\");t.forEach((r,n)=>{if(!e.isValid(r))throw new Error(\"invalid scalar at index \"+n)})}var fe=new WeakMap,ze=new WeakMap;function ae(t){return ze.get(t)||1}function Ge(t){if(t!==yt)throw new Error(\"invalid wNAF\")}var Mt=class{constructor(e,r){this.BASE=e.BASE,this.ZERO=e.ZERO,this.Fn=e.Fn,this.bits=r}_unsafeLadder(e,r,n=this.ZERO){let o=e;for(;r>yt;)r&dt&&(n=n.add(o)),o=o.double(),r>>=dt;return n}precomputeWindow(e,r){let{windows:n,windowSize:o}=ce(r,this.bits),i=[],s=e,c=s;for(let f=0;f<n;f++){c=s,i.push(c);for(let b=1;b<o;b++)c=c.add(s),i.push(c);s=c.double()}return i}wNAF(e,r,n){if(!this.Fn.isValid(n))throw new Error(\"invalid scalar\");let o=this.ZERO,i=this.BASE,s=ce(e,this.bits);for(let c=0;c<s.windows;c++){let{nextN:f,offset:b,isZero:x,isNeg:g,isNegF:a,offsetF:l}=Ke(n,c,s);n=f,x?i=i.add(It(a,r[l])):o=o.add(It(g,r[b]))}return Ge(n),{p:o,f:i}}wNAFUnsafe(e,r,n,o=this.ZERO){let i=ce(e,this.bits);for(let s=0;s<i.windows&&n!==yt;s++){let{nextN:c,offset:f,isZero:b,isNeg:x}=Ke(n,s,i);if(n=c,!b){let g=r[f];o=o.add(x?g.negate():g)}}return Ge(n),o}getPrecomputes(e,r,n){let o=fe.get(r);return o||(o=this.precomputeWindow(r,e),e!==1&&(typeof n==\"function\"&&(o=n(o)),fe.set(r,o))),o}cached(e,r,n){let o=ae(e);return this.wNAF(o,this.getPrecomputes(o,e,n),r)}unsafe(e,r,n,o){let i=ae(e);return i===1?this._unsafeLadder(e,r,o):this.wNAFUnsafe(i,this.getPrecomputes(i,e,n),r,o)}createCache(e,r){Ye(r,this.bits),ze.set(e,r),fe.delete(e)}hasCache(e){return ae(e)!==1}};function Pe(t,e,r,n){let o=e,i=t.ZERO,s=t.ZERO;for(;r>yt||n>yt;)r&dt&&(i=i.add(o)),n&dt&&(s=s.add(o)),o=o.double(),r>>=dt,n>>=dt;return{p1:i,p2:s}}function We(t,e,r,n){Un(r,t),kn(n,e);let o=r.length,i=n.length;if(o!==i)throw new Error(\"arrays of points and scalars must have equal length\");let s=t.ZERO,c=Dt(BigInt(o)),f=1;c>12?f=c-3:c>4?f=c-2:c>0&&(f=2);let b=nt(f),x=new Array(Number(b)+1).fill(s),g=Math.floor((e.BITS-1)/f)*f,a=s;for(let l=g;l>=0;l-=f){x.fill(s);for(let E=0;E<i;E++){let L=n[E],T=Number(L>>BigInt(l)&b);x[T]=x[T].add(r[E])}let w=s;for(let E=x.length-1,L=s;E>0;E--)L=L.add(x[E]),w=w.add(L);if(a=a.add(w),l!==0)for(let E=0;E<f;E++)a=a.double()}return a}function Xe(t,e,r){if(e){if(e.ORDER!==t)throw new Error(\"Field.ORDER must match order: Fp == p, Fn == n\");return oe(e),e}else return rt(t,{isLE:r})}function $e(t,e,r={},n){if(n===void 0&&(n=t===\"edwards\"),!e||typeof e!=\"object\")throw new Error(`expected valid ${t} CURVE object`);for(let f of[\"p\",\"n\",\"h\"]){let b=e[f];if(!(typeof b==\"bigint\"&&b>yt))throw new Error(`CURVE.${f} must be positive bigint`)}let o=Xe(e.p,r.Fp,n),i=Xe(e.n,r.Fn,n),c=[\"Gx\",\"Gy\",\"a\",t===\"weierstrass\"?\"b\":\"d\"];for(let f of c)if(!o.isValid(e[f]))throw new Error(`CURVE.${f} must be valid field element of CURVE.Fp`);return e=Object.freeze(Object.assign({},e)),{CURVE:e,Fp:o,Fn:i}}var Qe=(t,e)=>(t+(t>=0?e:-e)/Je)/e;function Tn(t,e,r){let[[n,o],[i,s]]=e,c=Qe(s*t,r),f=Qe(-o*t,r),b=t-c*n-f*i,x=-c*o-f*s,g=b<J,a=x<J;g&&(b=-b),a&&(x=-x);let l=nt(Math.ceil(Dt(r)/2))+mt;if(b<J||b>=l||x<J||x>=l)throw new Error(\"splitScalar (endomorphism): failed, k=\"+t);return{k1neg:g,k1:b,k2neg:a,k2:x}}function le(t){if(![\"compact\",\"recovered\",\"der\"].includes(t))throw new Error('Signature format must be \"compact\", \"recovered\", or \"der\"');return t}function ue(t,e){let r={};for(let n of Object.keys(e))r[n]=t[n]===void 0?e[n]:t[n];return St(r.lowS,\"lowS\"),St(r.prehash,\"prehash\"),r.format!==void 0&&le(r.format),r}var de=class extends Error{constructor(e=\"\"){super(e)}},Q={Err:de,_tlv:{encode:(t,e)=>{let{Err:r}=Q;if(t<0||t>256)throw new r(\"tlv.encode: wrong tag\");if(e.length&1)throw new r(\"tlv.encode: unpadded data\");let n=e.length/2,o=At(n);if(o.length/2&128)throw new r(\"tlv.encode: long form length too big\");let i=n>127?At(o.length/2|128):\"\";return At(t)+i+o+e},decode(t,e){let{Err:r}=Q,n=0;if(t<0||t>256)throw new r(\"tlv.encode: wrong tag\");if(e.length<2||e[n++]!==t)throw new r(\"tlv.decode: wrong tlv\");let o=e[n++],i=!!(o&128),s=0;if(!i)s=o;else{let f=o&127;if(!f)throw new r(\"tlv.decode(long): indefinite length not supported\");if(f>4)throw new r(\"tlv.decode(long): byte length is too big\");let b=e.subarray(n,n+f);if(b.length!==f)throw new r(\"tlv.decode: length bytes not complete\");if(b[0]===0)throw new r(\"tlv.decode(long): zero leftmost byte\");for(let x of b)s=s<<8|x;if(n+=f,s<128)throw new r(\"tlv.decode(long): not minimal encoding\")}let c=e.subarray(n,n+s);if(c.length!==s)throw new r(\"tlv.decode: wrong value length\");return{v:c,l:e.subarray(n+s)}}},_int:{encode(t){let{Err:e}=Q;if(t<J)throw new e(\"integer: negative integers are not allowed\");let r=At(t);if(Number.parseInt(r[0],16)&8&&(r=\"00\"+r),r.length&1)throw new e(\"unexpected DER parsing assertion: unpadded hex\");return r},decode(t){let{Err:e}=Q;if(t[0]&128)throw new e(\"invalid signature integer: negative\");if(t[0]===0&&!(t[1]&128))throw new e(\"invalid signature integer: unnecessary leading zero\");return gt(t)}},toSig(t){let{Err:e,_int:r,_tlv:n}=Q,o=V(\"signature\",t),{v:i,l:s}=n.decode(48,o);if(s.length)throw new e(\"invalid signature: left bytes after parsing\");let{v:c,l:f}=n.decode(2,i),{v:b,l:x}=n.decode(2,f);if(x.length)throw new e(\"invalid signature: left bytes after parsing\");return{r:r.decode(c),s:r.decode(b)}},hexFromSig(t){let{_tlv:e,_int:r}=Q,n=e.encode(2,r.encode(t.r)),o=e.encode(2,r.encode(t.s)),i=n+o;return e.encode(48,i)}},J=BigInt(0),mt=BigInt(1),Je=BigInt(2),Gt=BigInt(3),Rn=BigInt(4);function wt(t,e){let{BYTES:r}=t,n;if(typeof e==\"bigint\")n=e;else{let o=V(\"private key\",e);try{n=t.fromBytes(o)}catch{throw new Error(`invalid private key: expected ui8a of size ${r}, got ${typeof e}`)}}if(!t.isValidNot0(n))throw new Error(\"invalid private key: out of range [1..N-1]\");return n}function qn(t,e={}){let r=$e(\"weierstrass\",t,e),{Fp:n,Fn:o}=r,i=r.CURVE,{h:s,n:c}=i;_t(e,{},{allowInfinityPoint:\"boolean\",clearCofactor:\"function\",isTorsionFree:\"function\",fromBytes:\"function\",toBytes:\"function\",endo:\"object\",wrapPrivateKey:\"boolean\"});let{endo:f}=e;if(f&&(!n.is0(i.a)||typeof f.beta!=\"bigint\"||!Array.isArray(f.basises)))throw new Error('invalid endo: expected \"beta\": bigint and \"basises\": array');let b=tn(n,o);function x(){if(!n.isOdd)throw new Error(\"compression is not supported: Field does not have .isOdd()\")}function g(H,h,d){let{x:u,y:p}=h.toAffine(),y=n.toBytes(u);if(St(d,\"isCompressed\"),d){x();let v=!n.isOdd(p);return Y(Fe(v),y)}else return Y(Uint8Array.of(4),y,n.toBytes(p))}function a(H){et(H,void 0,\"Point\");let{publicKey:h,publicKeyUncompressed:d}=b,u=H.length,p=H[0],y=H.subarray(1);if(u===h&&(p===2||p===3)){let v=n.fromBytes(y);if(!n.isValid(v))throw new Error(\"bad point: is not on curve, wrong x\");let B=E(v),m;try{m=n.sqrt(B)}catch(q){let O=q instanceof Error?\": \"+q.message:\"\";throw new Error(\"bad point: is not on curve, sqrt error\"+O)}x();let S=n.isOdd(m);return(p&1)===1!==S&&(m=n.neg(m)),{x:v,y:m}}else if(u===d&&p===4){let v=n.BYTES,B=n.fromBytes(y.subarray(0,v)),m=n.fromBytes(y.subarray(v,v*2));if(!L(B,m))throw new Error(\"bad point: is not on curve\");return{x:B,y:m}}else throw new Error(`bad point: got length ${u}, expected compressed=${h} or uncompressed=${d}`)}let l=e.toBytes||g,w=e.fromBytes||a;function E(H){let h=n.sqr(H),d=n.mul(h,H);return n.add(n.add(d,n.mul(H,i.a)),i.b)}function L(H,h){let d=n.sqr(h),u=E(H);return n.eql(d,u)}if(!L(i.Gx,i.Gy))throw new Error(\"bad curve params: generator point\");let T=n.mul(n.pow(i.a,Gt),Rn),Bt=n.mul(n.sqr(i.b),BigInt(27));if(n.is0(n.add(T,Bt)))throw new Error(\"bad curve params: a or b\");function R(H,h,d=!1){if(!n.isValid(h)||d&&n.is0(h))throw new Error(`bad point coordinate ${H}`);return h}function st(H){if(!(H instanceof _))throw new Error(\"ProjectivePoint expected\")}function F(H){if(!f||!f.basises)throw new Error(\"no endo\");return Tn(H,f.basises,o.ORDER)}let ht=ne((H,h)=>{let{X:d,Y:u,Z:p}=H;if(n.eql(p,n.ONE))return{x:d,y:u};let y=H.is0();h==null&&(h=y?n.ONE:n.inv(p));let v=n.mul(d,h),B=n.mul(u,h),m=n.mul(p,h);if(y)return{x:n.ZERO,y:n.ZERO};if(!n.eql(m,n.ONE))throw new Error(\"invZ was invalid\");return{x:v,y:B}}),Ot=ne(H=>{if(H.is0()){if(e.allowInfinityPoint&&!n.is0(H.Y))return;throw new Error(\"bad point: ZERO\")}let{x:h,y:d}=H.toAffine();if(!n.isValid(h)||!n.isValid(d))throw new Error(\"bad point: x or y not field elements\");if(!L(h,d))throw new Error(\"bad point: equation left != right\");if(!H.isTorsionFree())throw new Error(\"bad point: not in prime-order subgroup\");return!0});function bt(H,h,d,u,p){return d=new _(n.mul(d.X,H),d.Y,d.Z),h=It(u,h),d=It(p,d),h.add(d)}class _{constructor(h,d,u){this.X=R(\"x\",h),this.Y=R(\"y\",d,!0),this.Z=R(\"z\",u),Object.freeze(this)}static CURVE(){return i}static fromAffine(h){let{x:d,y:u}=h||{};if(!h||!n.isValid(d)||!n.isValid(u))throw new Error(\"invalid affine point\");if(h instanceof _)throw new Error(\"projective point not allowed\");return n.is0(d)&&n.is0(u)?_.ZERO:new _(d,u,n.ONE)}static fromBytes(h){let d=_.fromAffine(w(et(h,void 0,\"point\")));return d.assertValidity(),d}static fromHex(h){return _.fromBytes(V(\"pointHex\",h))}get x(){return this.toAffine().x}get y(){return this.toAffine().y}precompute(h=8,d=!0){return it.createCache(this,h),d||this.multiply(Gt),this}assertValidity(){Ot(this)}hasEvenY(){let{y:h}=this.toAffine();if(!n.isOdd)throw new Error(\"Field doesn't support isOdd\");return!n.isOdd(h)}equals(h){st(h);let{X:d,Y:u,Z:p}=this,{X:y,Y:v,Z:B}=h,m=n.eql(n.mul(d,B),n.mul(y,p)),S=n.eql(n.mul(u,B),n.mul(v,p));return m&&S}negate(){return new _(this.X,n.neg(this.Y),this.Z)}double(){let{a:h,b:d}=i,u=n.mul(d,Gt),{X:p,Y:y,Z:v}=this,B=n.ZERO,m=n.ZERO,S=n.ZERO,A=n.mul(p,p),q=n.mul(y,y),O=n.mul(v,v),I=n.mul(p,y);return I=n.add(I,I),S=n.mul(p,v),S=n.add(S,S),B=n.mul(h,S),m=n.mul(u,O),m=n.add(B,m),B=n.sub(q,m),m=n.add(q,m),m=n.mul(B,m),B=n.mul(I,B),S=n.mul(u,S),O=n.mul(h,O),I=n.sub(A,O),I=n.mul(h,I),I=n.add(I,S),S=n.add(A,A),A=n.add(S,A),A=n.add(A,O),A=n.mul(A,I),m=n.add(m,A),O=n.mul(y,v),O=n.add(O,O),A=n.mul(O,I),B=n.sub(B,A),S=n.mul(O,q),S=n.add(S,S),S=n.add(S,S),new _(B,m,S)}add(h){st(h);let{X:d,Y:u,Z:p}=this,{X:y,Y:v,Z:B}=h,m=n.ZERO,S=n.ZERO,A=n.ZERO,q=i.a,O=n.mul(i.b,Gt),I=n.mul(d,y),U=n.mul(u,v),N=n.mul(p,B),j=n.add(d,u),k=n.add(y,v);j=n.mul(j,k),k=n.add(I,U),j=n.sub(j,k),k=n.add(d,p);let C=n.add(y,B);return k=n.mul(k,C),C=n.add(I,N),k=n.sub(k,C),C=n.add(u,p),m=n.add(v,B),C=n.mul(C,m),m=n.add(U,N),C=n.sub(C,m),A=n.mul(q,k),m=n.mul(O,N),A=n.add(m,A),m=n.sub(U,A),A=n.add(U,A),S=n.mul(m,A),U=n.add(I,I),U=n.add(U,I),N=n.mul(q,N),k=n.mul(O,k),U=n.add(U,N),N=n.sub(I,N),N=n.mul(q,N),k=n.add(k,N),I=n.mul(U,k),S=n.add(S,I),I=n.mul(C,k),m=n.mul(j,m),m=n.sub(m,I),I=n.mul(j,U),A=n.mul(C,A),A=n.add(A,I),new _(m,S,A)}subtract(h){return this.add(h.negate())}is0(){return this.equals(_.ZERO)}multiply(h){let{endo:d}=e;if(!o.isValidNot0(h))throw new Error(\"invalid scalar: out of range\");let u,p,y=v=>it.cached(this,v,B=>Kt(_,B));if(d){let{k1neg:v,k1:B,k2neg:m,k2:S}=F(h),{p:A,f:q}=y(B),{p:O,f:I}=y(S);p=q.add(I),u=bt(d.beta,A,O,v,m)}else{let{p:v,f:B}=y(h);u=v,p=B}return Kt(_,[u,p])[0]}multiplyUnsafe(h){let{endo:d}=e,u=this;if(!o.isValid(h))throw new Error(\"invalid scalar: out of range\");if(h===J||u.is0())return _.ZERO;if(h===mt)return u;if(it.hasCache(this))return this.multiply(h);if(d){let{k1neg:p,k1:y,k2neg:v,k2:B}=F(h),{p1:m,p2:S}=Pe(_,u,y,B);return bt(d.beta,m,S,p,v)}else return it.unsafe(u,h)}multiplyAndAddUnsafe(h,d,u){let p=this.multiplyUnsafe(d).add(h.multiplyUnsafe(u));return p.is0()?void 0:p}toAffine(h){return ht(this,h)}isTorsionFree(){let{isTorsionFree:h}=e;return s===mt?!0:h?h(_,this):it.unsafe(this,c).is0()}clearCofactor(){let{clearCofactor:h}=e;return s===mt?this:h?h(_,this):this.multiplyUnsafe(s)}isSmallOrder(){return this.multiplyUnsafe(s).is0()}toBytes(h=!0){return St(h,\"isCompressed\"),this.assertValidity(),l(_,this,h)}toHex(h=!0){return W(this.toBytes(h))}toString(){return`<Point ${this.is0()?\"ZERO\":this.toHex()}>`}get px(){return this.X}get py(){return this.X}get pz(){return this.Z}toRawBytes(h=!0){return this.toBytes(h)}_setWindowSize(h){this.precompute(h)}static normalizeZ(h){return Kt(_,h)}static msm(h,d){return We(_,o,h,d)}static fromPrivateKey(h){return _.BASE.multiply(wt(o,h))}}_.BASE=new _(i.Gx,i.Gy,n.ONE),_.ZERO=new _(n.ZERO,n.ONE,n.ZERO),_.Fp=n,_.Fn=o;let Ut=o.BITS,it=new Mt(_,e.endo?Math.ceil(Ut/2):Ut);return _.BASE.precompute(8),_}function Fe(t){return Uint8Array.of(t?2:3)}function tn(t,e){return{secretKey:e.BYTES,publicKey:1+t.BYTES,publicKeyUncompressed:1+2*t.BYTES,publicKeyHasPrefix:!0,signature:2*e.BYTES}}function Nn(t,e={}){let{Fn:r}=t,n=e.randomBytes||qt,o=Object.assign(tn(t.Fp,r),{seed:se(r.ORDER)});function i(l){try{return!!wt(r,l)}catch{return!1}}function s(l,w){let{publicKey:E,publicKeyUncompressed:L}=o;try{let T=l.length;return w===!0&&T!==E||w===!1&&T!==L?!1:!!t.fromBytes(l)}catch{return!1}}function c(l=n(o.seed)){return ie(et(l,o.seed,\"seed\"),r.ORDER)}function f(l,w=!0){return t.BASE.multiply(wt(r,l)).toBytes(w)}function b(l){let w=c(l);return{secretKey:w,publicKey:f(w)}}function x(l){if(typeof l==\"bigint\")return!1;if(l instanceof t)return!0;let{secretKey:w,publicKey:E,publicKeyUncompressed:L}=o;if(r.allowedLengths||w===E)return;let T=V(\"key\",l).length;return T===E||T===L}function g(l,w,E=!0){if(x(l)===!0)throw new Error(\"first arg must be private key\");if(x(w)===!1)throw new Error(\"second arg must be public key\");let L=wt(r,l);return t.fromHex(w).multiply(L).toBytes(E)}return Object.freeze({getPublicKey:f,getSharedSecret:g,keygen:b,Point:t,utils:{isValidSecretKey:i,isValidPublicKey:s,randomSecretKey:c,isValidPrivateKey:i,randomPrivateKey:c,normPrivateKeyToScalar:l=>wt(r,l),precompute(l=8,w=t.BASE){return w.precompute(l,!1)}},lengths:o})}function Cn(t,e,r={}){Tt(e),_t(r,{},{hmac:\"function\",lowS:\"boolean\",randomBytes:\"function\",bits2int:\"function\",bits2int_modN:\"function\"});let n=r.randomBytes||qt,o=r.hmac||((d,...u)=>$t(e,d,Y(...u))),{Fp:i,Fn:s}=t,{ORDER:c,BITS:f}=s,{keygen:b,getPublicKey:x,getSharedSecret:g,utils:a,lengths:l}=Nn(t,r),w={prehash:!1,lowS:typeof r.lowS==\"boolean\"?r.lowS:!1,format:void 0,extraEntropy:!1},E=\"compact\";function L(d){let u=c>>mt;return d>u}function T(d,u){if(!s.isValidNot0(u))throw new Error(`invalid signature ${d}: out of range 1..Point.Fn.ORDER`);return u}function Bt(d,u){le(u);let p=l.signature,y=u===\"compact\"?p:u===\"recovered\"?p+1:void 0;return et(d,y,`${u} signature`)}class R{constructor(u,p,y){this.r=T(\"r\",u),this.s=T(\"s\",p),y!=null&&(this.recovery=y),Object.freeze(this)}static fromBytes(u,p=E){Bt(u,p);let y;if(p===\"der\"){let{r:S,s:A}=Q.toSig(et(u));return new R(S,A)}p===\"recovered\"&&(y=u[0],p=\"compact\",u=u.subarray(1));let v=s.BYTES,B=u.subarray(0,v),m=u.subarray(v,v*2);return new R(s.fromBytes(B),s.fromBytes(m),y)}static fromHex(u,p){return this.fromBytes(ut(u),p)}addRecoveryBit(u){return new R(this.r,this.s,u)}recoverPublicKey(u){let p=i.ORDER,{r:y,s:v,recovery:B}=this;if(B==null||![0,1,2,3].includes(B))throw new Error(\"recovery id invalid\");if(c*Je<p&&B>1)throw new Error(\"recovery id is ambiguous for h>1 curve\");let S=B===2||B===3?y+c:y;if(!i.isValid(S))throw new Error(\"recovery id 2 or 3 invalid\");let A=i.toBytes(S),q=t.fromBytes(Y(Fe((B&1)===0),A)),O=s.inv(S),I=F(V(\"msgHash\",u)),U=s.create(-I*O),N=s.create(v*O),j=t.BASE.multiplyUnsafe(U).add(q.multiplyUnsafe(N));if(j.is0())throw new Error(\"point at infinify\");return j.assertValidity(),j}hasHighS(){return L(this.s)}toBytes(u=E){if(le(u),u===\"der\")return ut(Q.hexFromSig(this));let p=s.toBytes(this.r),y=s.toBytes(this.s);if(u===\"recovered\"){if(this.recovery==null)throw new Error(\"recovery bit must be present\");return Y(Uint8Array.of(this.recovery),p,y)}return Y(p,y)}toHex(u){return W(this.toBytes(u))}assertValidity(){}static fromCompact(u){return R.fromBytes(V(\"sig\",u),\"compact\")}static fromDER(u){return R.fromBytes(V(\"sig\",u),\"der\")}normalizeS(){return this.hasHighS()?new R(this.r,s.neg(this.s),this.recovery):this}toDERRawBytes(){return this.toBytes(\"der\")}toDERHex(){return W(this.toBytes(\"der\"))}toCompactRawBytes(){return this.toBytes(\"compact\")}toCompactHex(){return W(this.toBytes(\"compact\"))}}let st=r.bits2int||function(u){if(u.length>8192)throw new Error(\"input is too large\");let p=gt(u),y=u.length*8-f;return y>0?p>>BigInt(y):p},F=r.bits2int_modN||function(u){return s.create(st(u))},ht=nt(f);function Ot(d){return Ue(\"num < 2^\"+f,d,J,ht),s.toBytes(d)}function bt(d,u){return et(d,void 0,\"message\"),u?et(e(d),void 0,\"prehashed message\"):d}function _(d,u,p){if([\"recovered\",\"canonical\"].some(U=>U in p))throw new Error(\"sign() legacy options not supported\");let{lowS:y,prehash:v,extraEntropy:B}=ue(p,w);d=bt(d,v);let m=F(d),S=wt(s,u),A=[Ot(S),Ot(m)];if(B!=null&&B!==!1){let U=B===!0?n(l.secretKey):B;A.push(V(\"extraEntropy\",U))}let q=Y(...A),O=m;function I(U){let N=st(U);if(!s.isValidNot0(N))return;let j=s.inv(N),k=t.BASE.multiply(N).toAffine(),C=s.create(k.x);if(C===J)return;let kt=s.create(j*s.create(O+C*S));if(kt===J)return;let we=(k.x===C?0:2)|Number(k.y&mt),me=kt;return y&&L(kt)&&(me=s.neg(kt),we^=1),new R(C,me,we)}return{seed:q,k2sig:I}}function Ut(d,u,p={}){d=V(\"message\",d);let{seed:y,k2sig:v}=_(d,u,p);return ke(e.outputLen,s.BYTES,o)(y,v)}function it(d){let u,p=typeof d==\"string\"||ft(d),y=!p&&d!==null&&typeof d==\"object\"&&typeof d.r==\"bigint\"&&typeof d.s==\"bigint\";if(!p&&!y)throw new Error(\"invalid signature, expected Uint8Array, hex string or Signature instance\");if(y)u=new R(d.r,d.s);else if(p){try{u=R.fromBytes(V(\"sig\",d),\"der\")}catch(v){if(!(v instanceof Q.Err))throw v}if(!u)try{u=R.fromBytes(V(\"sig\",d),\"compact\")}catch{return!1}}return u||!1}function H(d,u,p,y={}){let{lowS:v,prehash:B,format:m}=ue(y,w);if(p=V(\"publicKey\",p),u=bt(V(\"message\",u),B),\"strict\"in y)throw new Error(\"options.strict was renamed to lowS\");let S=m===void 0?it(d):R.fromBytes(V(\"sig\",d),m);if(S===!1)return!1;try{let A=t.fromBytes(p);if(v&&S.hasHighS())return!1;let{r:q,s:O}=S,I=F(u),U=s.inv(O),N=s.create(I*U),j=s.create(q*U),k=t.BASE.multiplyUnsafe(N).add(A.multiplyUnsafe(j));return k.is0()?!1:s.create(k.x)===q}catch{return!1}}function h(d,u,p={}){let{prehash:y}=ue(p,w);return u=bt(u,y),R.fromBytes(d,\"recovered\").recoverPublicKey(u).toBytes()}return Object.freeze({keygen:b,getPublicKey:x,getSharedSecret:g,utils:a,lengths:l,Point:t,sign:Ut,verify:H,recoverPublicKey:h,Signature:R,hash:e})}function Vn(t){let e={a:t.a,b:t.b,p:t.Fp.ORDER,n:t.n,h:t.h,Gx:t.Gx,Gy:t.Gy},r=t.Fp,n=t.allowedPrivateKeyLengths?Array.from(new Set(t.allowedPrivateKeyLengths.map(s=>Math.ceil(s/2)))):void 0,o=rt(e.n,{BITS:t.nBitLength,allowedLengths:n,modFromBytes:t.wrapPrivateKey}),i={Fp:r,Fn:o,allowInfinityPoint:t.allowInfinityPoint,endo:t.endo,isTorsionFree:t.isTorsionFree,clearCofactor:t.clearCofactor,fromBytes:t.fromBytes,toBytes:t.toBytes};return{CURVE:e,curveOpts:i}}function Dn(t){let{CURVE:e,curveOpts:r}=Vn(t),n={hmac:t.hmac,randomBytes:t.randomBytes,lowS:t.lowS,bits2int:t.bits2int,bits2int_modN:t.bits2int_modN};return{CURVE:e,curveOpts:r,hash:t.hash,ecdsaOpts:n}}function Zn(t,e){let r=e.Point;return Object.assign({},e,{ProjectivePoint:r,CURVE:Object.assign({},t,jt(r.Fn.ORDER,r.Fn.BITS))})}function en(t){let{CURVE:e,curveOpts:r,hash:n,ecdsaOpts:o}=Dn(t),i=qn(e,r),s=Cn(i,n,o);return Zn(t,s)}function nn(t,e){let r=n=>en({...t,hash:n});return{...r(e),create:r}}var be={p:BigInt(\"0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f\"),n:BigInt(\"0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141\"),h:BigInt(1),a:BigInt(0),b:BigInt(7),Gx:BigInt(\"0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798\"),Gy:BigInt(\"0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8\")},jn={beta:BigInt(\"0x7ae96a2b657c07106e64479eac3434e99cf0497512f58995c1396c28719501ee\"),basises:[[BigInt(\"0x3086d221a7d46bcde86c90e49284eb15\"),-BigInt(\"0xe4437ed6010e88286f547fa90abfe4c3\")],[BigInt(\"0x114ca50f7a8e2f3f657c1108d9d44cfd8\"),BigInt(\"0x3086d221a7d46bcde86c90e49284eb15\")]]};var rn=BigInt(2);function Mn(t){let e=be.p,r=BigInt(3),n=BigInt(6),o=BigInt(11),i=BigInt(22),s=BigInt(23),c=BigInt(44),f=BigInt(88),b=t*t*t%e,x=b*b*t%e,g=M(x,r,e)*x%e,a=M(g,r,e)*x%e,l=M(a,rn,e)*b%e,w=M(l,o,e)*l%e,E=M(w,i,e)*w%e,L=M(E,c,e)*E%e,T=M(L,f,e)*L%e,Bt=M(T,c,e)*E%e,R=M(Bt,r,e)*x%e,st=M(R,s,e)*w%e,F=M(st,n,e)*b%e,ht=M(F,rn,e);if(!he.eql(he.sqr(ht),t))throw new Error(\"Cannot find square root\");return ht}var he=rt(be.p,{sqrt:Mn}),Kn=nn({...be,Fp:he,lowS:!0,endo:jn},He);function xe(t){if(!Number.isSafeInteger(t)||t<0)throw new Error(\"positive integer expected, got \"+t)}function Gn(t){return t instanceof Uint8Array||ArrayBuffer.isView(t)&&t.constructor.name===\"Uint8Array\"}function Ht(t,...e){if(!Gn(t))throw new Error(\"Uint8Array expected\");if(e.length>0&&!e.includes(t.length))throw new Error(\"Uint8Array expected of length \"+e+\", got length=\"+t.length)}function pe(t,e=!0){if(t.destroyed)throw new Error(\"Hash instance has been destroyed\");if(e&&t.finished)throw new Error(\"Hash#digest() has already been called\")}function on(t,e){Ht(t);let r=e.outputLen;if(t.length<r)throw new Error(\"digestInto() expects output buffer of length at least \"+r)}var Xt=BigInt(4294967295),sn=BigInt(32);function Xn(t,e=!1){return e?{h:Number(t&Xt),l:Number(t>>sn&Xt)}:{h:Number(t>>sn&Xt)|0,l:Number(t&Xt)|0}}function cn(t,e=!1){let r=new Uint32Array(t.length),n=new Uint32Array(t.length);for(let o=0;o<t.length;o++){let{h:i,l:s}=Xn(t[o],e);[r[o],n[o]]=[i,s]}return[r,n]}var fn=(t,e,r)=>t<<r|e>>>32-r,an=(t,e,r)=>e<<r|t>>>32-r,un=(t,e,r)=>e<<r-32|t>>>64-r,ln=(t,e,r)=>t<<r-32|e>>>64-r;function dn(t){return new Uint32Array(t.buffer,t.byteOffset,Math.floor(t.byteLength/4))}var ge=new Uint8Array(new Uint32Array([287454020]).buffer)[0]===68;function Yn(t){return t<<24&4278190080|t<<8&16711680|t>>>8&65280|t>>>24&255}function ye(t){for(let e=0;e<t.length;e++)t[e]=Yn(t[e])}function zn(t){if(typeof t!=\"string\")throw new Error(\"utf8ToBytes expected string, got \"+typeof t);return new Uint8Array(new TextEncoder().encode(t))}function zt(t){return typeof t==\"string\"&&(t=zn(t)),Ht(t),t}var Yt=class{clone(){return this._cloneInto()}};function hn(t){let e=n=>t().update(zt(n)).digest(),r=t();return e.outputLen=r.outputLen,e.blockLen=r.blockLen,e.create=()=>t(),e}function bn(t){let e=(n,o)=>t(o).update(zt(n)).digest(),r=t({});return e.outputLen=r.outputLen,e.blockLen=r.blockLen,e.create=n=>t(n),e}var gn=[],yn=[],wn=[],Pn=BigInt(0),Lt=BigInt(1),Wn=BigInt(2),$n=BigInt(7),Qn=BigInt(256),Jn=BigInt(113);for(let t=0,e=Lt,r=1,n=0;t<24;t++){[r,n]=[n,(2*r+3*n)%5],gn.push(2*(5*n+r)),yn.push((t+1)*(t+2)/2%64);let o=Pn;for(let i=0;i<7;i++)e=(e<<Lt^(e>>$n)*Jn)%Qn,e&Wn&&(o^=Lt<<(Lt<<BigInt(i))-Lt);wn.push(o)}var[Fn,tr]=cn(wn,!0),xn=(t,e,r)=>r>32?un(t,e,r):fn(t,e,r),pn=(t,e,r)=>r>32?ln(t,e,r):an(t,e,r);function er(t,e=24){let r=new Uint32Array(10);for(let n=24-e;n<24;n++){for(let s=0;s<10;s++)r[s]=t[s]^t[s+10]^t[s+20]^t[s+30]^t[s+40];for(let s=0;s<10;s+=2){let c=(s+8)%10,f=(s+2)%10,b=r[f],x=r[f+1],g=xn(b,x,1)^r[c],a=pn(b,x,1)^r[c+1];for(let l=0;l<50;l+=10)t[s+l]^=g,t[s+l+1]^=a}let o=t[2],i=t[3];for(let s=0;s<24;s++){let c=yn[s],f=xn(o,i,c),b=pn(o,i,c),x=gn[s];o=t[x],i=t[x+1],t[x]=f,t[x+1]=b}for(let s=0;s<50;s+=10){for(let c=0;c<10;c++)r[c]=t[s+c];for(let c=0;c<10;c++)t[s+c]^=~r[(c+2)%10]&r[(c+4)%10]}t[0]^=Fn[n],t[1]^=tr[n]}r.fill(0)}var Pt=class t extends Yt{constructor(e,r,n,o=!1,i=24){if(super(),this.blockLen=e,this.suffix=r,this.outputLen=n,this.enableXOF=o,this.rounds=i,this.pos=0,this.posOut=0,this.finished=!1,this.destroyed=!1,xe(n),0>=this.blockLen||this.blockLen>=200)throw new Error(\"Sha3 supports only keccak-f1600 function\");this.state=new Uint8Array(200),this.state32=dn(this.state)}keccak(){ge||ye(this.state32),er(this.state32,this.rounds),ge||ye(this.state32),this.posOut=0,this.pos=0}update(e){pe(this);let{blockLen:r,state:n}=this;e=zt(e);let o=e.length;for(let i=0;i<o;){let s=Math.min(r-this.pos,o-i);for(let c=0;c<s;c++)n[this.pos++]^=e[i++];this.pos===r&&this.keccak()}return this}finish(){if(this.finished)return;this.finished=!0;let{state:e,suffix:r,pos:n,blockLen:o}=this;e[n]^=r,(r&128)!==0&&n===o-1&&this.keccak(),e[o-1]^=128,this.keccak()}writeInto(e){pe(this,!1),Ht(e),this.finish();let r=this.state,{blockLen:n}=this;for(let o=0,i=e.length;o<i;){this.posOut>=n&&this.keccak();let s=Math.min(n-this.posOut,i-o);e.set(r.subarray(this.posOut,this.posOut+s),o),this.posOut+=s,o+=s}return e}xofInto(e){if(!this.enableXOF)throw new Error(\"XOF is not possible for this instance\");return this.writeInto(e)}xof(e){return xe(e),this.xofInto(new Uint8Array(e))}digestInto(e){if(on(e,this),this.finished)throw new Error(\"digest() was already called\");return this.writeInto(e),this.destroy(),e}digest(){return this.digestInto(new Uint8Array(this.outputLen))}destroy(){this.destroyed=!0,this.state.fill(0)}_cloneInto(e){let{blockLen:r,suffix:n,outputLen:o,rounds:i,enableXOF:s}=this;return e||(e=new t(r,n,o,s,i)),e.state32.set(this.state32),e.pos=this.pos,e.posOut=this.posOut,e.finished=this.finished,e.rounds=i,e.suffix=n,e.outputLen=o,e.enableXOF=s,e.destroyed=this.destroyed,e}},ot=(t,e,r)=>hn(()=>new Pt(e,t,r)),Xr=ot(6,144,224/8),Yr=ot(6,136,256/8),zr=ot(6,104,384/8),Pr=ot(6,72,512/8),Wr=ot(1,144,224/8),nr=ot(1,136,256/8),$r=ot(1,104,384/8),Qr=ot(1,72,512/8),mn=(t,e,r)=>bn((n={})=>new Pt(e,t,n.dkLen===void 0?r:n.dkLen,!0)),Jr=mn(31,168,128/8),Fr=mn(31,136,256/8);export{nr as keccak_256,Kn as secp256k1};\n/*! Bundled license information:\n\n@noble/hashes/esm/utils.js:\n@noble/hashes/esm/utils.js:\n  (*! noble-hashes - MIT License (c) 2022 Paul Miller (paulmillr.com) *)\n\n@noble/curves/esm/utils.js:\n@noble/curves/esm/abstract/modular.js:\n@noble/curves/esm/abstract/curve.js:\n@noble/curves/esm/abstract/weierstrass.js:\n@noble/curves/esm/_shortw_utils.js:\n@noble/curves/esm/secp256k1.js:\n  (*! noble-curves - MIT License (c) 2022 Paul Miller (paulmillr.com) *)\n*/\n";

let _noble;
async function loadNoble() {
  if (_noble !== undefined) return _noble;
  const dataUrl = `data:text/javascript;base64,${Buffer.from(VENDORED_NOBLE_SOURCE, "utf8").toString("base64")}`;
  const mod = await import(dataUrl);
  _noble = { secp256k1: mod.secp256k1, keccak_256: mod.keccak_256 };
  return _noble;
}

/** Uncompressed public key minus its 0x04 prefix, keccak256, low 20 bytes. */
function addressFromPrivateKey(noble, privateKeyBytes) {
  const publicKey = noble.secp256k1.getPublicKey(privateKeyBytes, false);
  const hash = noble.keccak_256(publicKey.slice(1));
  return bytesToHex(hash.slice(-20));
}

function encodeEip712Value(keccak256, type, value) {
  if (type === "string" || type === "bytes") {
    return keccak256(new TextEncoder().encode(String(value)));
  }
  if (/^uint\d*$/u.test(type) || /^int\d*$/u.test(type)) {
    return padTo32(BigInt(value));
  }
  if (type === "bool") {
    return padTo32(value ? 1n : 0n);
  }
  if (type === "address") {
    const clean = String(value).trim().replace(/^0x/iu, "").toLowerCase();
    return padTo32(BigInt(`0x${clean.padStart(40, "0")}`));
  }
  if (/^bytes\d+$/u.test(type)) {
    const bytes = hexToBytes(String(value));
    const out = new Uint8Array(32);
    out.set(bytes.slice(0, 32), 0);
    return out;
  }
  throw new Error(
    `This CLI's EIP-712 encoder does not support field type "${type}". It only implements what ` +
      "Ava's principal challenge actually uses (string, uint256); extend it deliberately before " +
      "signing anything of a wider type with it.",
  );
}

function eip712TypeHash(keccak256, typeName, types) {
  const fields = types?.[typeName];
  if (!fields) {
    throw new Error(`EIP-712 typed data is missing a type definition for "${typeName}".`);
  }
  const signature = `${typeName}(${fields.map((f) => `${f.type} ${f.name}`).join(",")})`;
  return keccak256(new TextEncoder().encode(signature));
}

function eip712HashStruct(keccak256, typeName, data, types) {
  const fields = types?.[typeName];
  if (!fields) {
    throw new Error(`EIP-712 typed data is missing a type definition for "${typeName}".`);
  }
  const parts = [eip712TypeHash(keccak256, typeName, types)];
  for (const field of fields) {
    parts.push(encodeEip712Value(keccak256, field.type, data?.[field.name]));
  }
  return keccak256(concatBytes(...parts));
}

/**
 * The EIP-712 digest of EXACTLY the typed data an API response carried.
 *
 * `domain`, `primaryType`, `types` and `message` are all read straight off
 * the server's response object and hashed as given — nothing here rebuilds
 * the challenge from separate fields the CLI already holds (nonce, label,
 * scopes, ...). A digest computed from a client-side reconstruction would let
 * a bug, or a compromised CLI, sign different terms than the ones the server
 * actually issued and the key holder believes they are approving.
 */
function hashTypedData(keccak256, typedData) {
  const { domain, primaryType, types, message } = typedData ?? {};
  if (domain === undefined || primaryType === undefined || types === undefined || message === undefined) {
    throw new Error("Typed data from the server is missing domain, primaryType, types, or message.");
  }
  const domainSeparator = eip712HashStruct(keccak256, "EIP712Domain", domain, types);
  const messageHash = eip712HashStruct(keccak256, primaryType, message, types);
  return bytesToHex(keccak256(concatBytes(Uint8Array.of(0x19, 0x01), domainSeparator, messageHash)));
}

/** ECDSA sign a 32-byte digest, low-s (non-malleable) by default — matches
 * what `recoverChallengeSigner` on the server requires. */
function signDigestHex(noble, digestHex, privateKeyBytes) {
  const signature = noble.secp256k1.sign(hexToBytes(digestHex), privateKeyBytes);
  const r = signature.r.toString(16).padStart(64, "0");
  const s = signature.s.toString(16).padStart(64, "0");
  const v = (27 + signature.recovery).toString(16).padStart(2, "0");
  return `0x${r}${s}${v}`;
}

function parseFlags(args) {
  const flags = {};
  for (let i = 0; i < args.length; i += 1) {
    const arg = args[i];
    if (!arg.startsWith("--")) continue;
    const key = arg.slice(2);
    const next = args[i + 1];
    if (next !== undefined && !next.startsWith("--")) {
      flags[key] = next;
      i += 1;
    } else {
      flags[key] = true;
    }
  }
  return flags;
}

async function http(method, path, { body, headers, auth = true } = {}) {
  const url = `${baseUrl()}${path}`;
  const bearer = auth ? token() : "";
  const credential = auth ? credentialSecret() : "";
  const res = await fetch(url, {
    method,
    headers: {
      "content-type": "application/json",
      accept: "application/json",
      ...(bearer ? { authorization: `Bearer ${bearer}` } : {}),
      // Mirrors the bearer above: attached automatically whenever one is
      // stored, on every authenticated call, not just a hardcoded allowlist
      // of "execute" paths. Routes that never check this header ignore it;
      // routes gated on it (copilot approve, lend execute, workflow execute)
      // finally see it without a second manual step per call.
      ...(credential ? { "x-ava-agent-credential": credential } : {}),
      ...(headers ?? {}),
    },
    body: body !== undefined ? JSON.stringify(body) : undefined,
  });
  const text = await res.text();
  let json;
  try {
    json = text ? JSON.parse(text) : null;
  } catch {
    json = { raw: text };
  }
  if (!res.ok) {
    const err = new Error(
      `HTTP ${res.status} ${method} ${path}: ${typeof json === "object" ? JSON.stringify(json) : text}`,
    );
    err.status = res.status;
    err.body = json;
    throw err;
  }
  return json;
}

async function mcpCall(name, args = {}) {
  const body = await http("POST", "/mcp", {
    body: {
      jsonrpc: "2.0",
      id: 1,
      method: "tools/call",
      params: { name, arguments: args },
    },
  });
  if (body?.error) {
    return { ok: false, error: body.error };
  }
  return body?.result?.structuredContent ?? body?.result ?? body;
}

function printJson(value) {
  console.log(JSON.stringify(value, null, 2));
}

async function cmdSession() {
  const displayName = env("AVA_DISPLAY_NAME", "openclaw-agent");
  // Deliberately unauthenticated: this is the call that hands out credentials,
  // and Ava's machine onboarding has no CAPTCHA, email, or wallet popup.
  const body = await http("POST", "/v1/users/session", {
    body: { displayName },
    auth: false,
  });
  const id =
    body?.user?.userId ??
    body?.userId ??
    body?.user?.id ??
    null;
  if (!id) {
    fail(`Session response missing userId: ${JSON.stringify(body)}`);
  }
  const issued = body?.token ?? null;
  if (!issued && !token()) {
    fail(
      `Session response carried no token and none is stored. Every other call needs one, so stopping here rather than making requests that will be refused: ${JSON.stringify(body)}`,
    );
  }
  // Written with mode 0600 by saveState. Treat this file as a secret.
  saveState({ userId: id, portal: portal(), ...(issued ? { token: issued } : {}) });
  printJson({
    ok: true,
    userId: id,
    portal: portal(),
    stateFile: STATE_FILE,
    tokenStored: Boolean(issued),
    note: "The token is stored in the state file (mode 0600) and is not printed here. It is shown by the API once and cannot be read back. Every other command sends it as Authorization: Bearer.",
    session: { ...body, token: issued ? "[stored, not printed]" : undefined },
  });
}

async function cmdTools() {
  const doc = await http("GET", "/mcp", { auth: false });
  const names = (doc.tools ?? []).map((t) => t.name);
  printJson({ ok: true, base: baseUrl(), tools: names, server: doc.server });
}

async function cmdTurn(message) {
  if (!message || !message.trim()) {
    fail('Usage: ava turn "Swap 10 USDC to SUI on sui with 50 bps slip"');
  }
  const uid = requireUserId();
  requireToken();
  const result = await mcpCall("ava_copilot_turn", {
    message: message.trim(),
    portal: portal(),
    userId: uid,
    mode: "testnet",
  });
  const actions = result?.actions ?? [];
  const approve = actions.find((a) => a?.type === "approve_execute");
  if (approve?.executionId) {
    saveState({ lastExecutionId: approve.executionId, userId: uid });
  }
  printJson({
    ...result,
    _hint:
      approve?.executionId !== undefined
        ? `Review quote. If user says yes: node scripts/ava.mjs approve ${approve.executionId}`
        : "No approve_execute action (parse failed or no trade). Do not invent a fill.",
  });
}

async function cmdApprove(executionId) {
  const id = executionId || loadState().lastExecutionId;
  if (!id) {
    fail("Usage: ava approve <executionId> (or run turn first to cache lastExecutionId)");
  }
  const uid = requireUserId();
  requireToken();
  const live = env("AVA_ENABLE_LIVE", "") === "true";
  const result = await mcpCall("ava_approve_execute", {
    executionId: id,
    userId: uid,
    portal: portal(),
    mode: live ? "mainnet" : "testnet",
  });
  printJson(result);
}

async function cmdPortfolio() {
  const uid = requireUserId();
  requireToken();
  printJson(
    await mcpCall("ava_portfolio", {
      userId: uid,
      portal: portal(),
    }),
  );
}

async function cmdPrice(asset) {
  if (!asset) fail("Usage: ava price SUI");
  printJson(
    await mcpCall("ava_get_price", {
      asset,
      vsCurrency: "usd",
    }),
  );
}

async function cmdCall(tool, jsonArgs) {
  if (!tool) fail("Usage: ava call <toolName> '<json args>'");
  let args = {};
  if (jsonArgs) {
    try {
      args = JSON.parse(jsonArgs);
    } catch (e) {
      fail(`Invalid JSON args: ${e.message}`);
    }
  }
  printJson(await mcpCall(tool, args));
}

async function cmdHealth() {
  try {
    const h = await http("GET", "/health", { auth: false });
    printJson({ ok: true, base: baseUrl(), health: h });
  } catch (e) {
    printJson({
      ok: false,
      base: baseUrl(),
      error: e.message,
      note: "Start api-worker: pnpm --filter @ava/api-worker dev (or your local start command)",
    });
    process.exit(1);
  }
}

/**
 * Obtain a scoped, 15-minute execute credential.
 *
 * Flow: POST /v1/principals/challenge (get EIP-712 typed data) → sign it
 * locally with the key the caller's mandates are signed with → POST
 * /v1/principals/verify (trade the signature for a credential). The secret is
 * stored in state.json (mode 0600) and printed nowhere; only scopes, audience
 * and expiry are shown, matching how `session` handles the bearer token.
 */
async function cmdCredential(rawArgs) {
  const flags = parseFlags(rawArgs);
  if (flags.key !== undefined) {
    fail(
      "Refusing --key: a raw private key must never be passed as a CLI argument. argv is visible " +
        "to every other process on the machine (ps, /proc/<pid>/cmdline, shell history). " +
        "Use --key-file <path> or --key-env <ENV_VAR_NAME>.",
    );
  }
  const keyFile = typeof flags["key-file"] === "string" ? flags["key-file"] : env("AVA_SIGNING_KEY_FILE");
  const keyEnvName = typeof flags["key-env"] === "string" ? flags["key-env"] : env("AVA_SIGNING_KEY_ENV");
  if (!keyFile && !keyEnvName) {
    fail(
      'Usage: ava credential --key-file <path> | --key-env <ENV_VAR_NAME> [--scopes execute] [--label "..."] [--chain-id 8453]\n' +
        "Or export AVA_SIGNING_KEY_FILE=<path> / AVA_SIGNING_KEY_ENV=<name>.\n" +
        "The key must be the same one your mandates are signed with. It is read from a file or an " +
        "environment variable, never from argv.",
    );
  }
  if (keyFile && keyEnvName) {
    fail("Pass exactly one of --key-file or --key-env (or their env equivalents), not both.");
  }

  const privateKey = readPrivateKey({ keyFile, keyEnvName });
  const noble = await loadNoble();
  const signerAddress = addressFromPrivateKey(noble, privateKey);

  requireUserId();
  requireToken();

  const scopes = (typeof flags.scopes === "string" ? flags.scopes : env("AVA_CREDENTIAL_SCOPES", "execute"))
    .split(",")
    .map((s) => s.trim())
    .filter((s) => s.length > 0);
  const label =
    typeof flags.label === "string" ? flags.label : env("AVA_DISPLAY_NAME", `openclaw-cli on ${hostname()}`);
  const chainIdFlag = typeof flags["chain-id"] === "string" ? Number(flags["chain-id"]) : undefined;

  const challenge = await http("POST", "/v1/principals/challenge", {
    body: {
      label,
      scopes,
      ...(chainIdFlag !== undefined && Number.isFinite(chainIdFlag) ? { chainId: chainIdFlag } : {}),
    },
  });

  const typedData = challenge?.typedData;
  const nonce = challenge?.nonce;
  if (!typedData || !nonce) {
    fail(`Challenge response carried no typedData or nonce: ${JSON.stringify(challenge)}`);
  }

  const expectedSigner = String(challenge.signWith ?? "").toLowerCase();
  if (expectedSigner.length > 0 && expectedSigner !== signerAddress.toLowerCase()) {
    fail(
      `This key signs as ${signerAddress}, but Ava expects the address your mandates are signed ` +
        `with: ${expectedSigner}. A credential is only ever issued to that key. Point --key-file / ` +
        "--key-env at it, or sign a mandate with this key first.",
    );
  }

  // Digest computed from EXACTLY what the server returned above — see
  // hashTypedData's own comment for why nothing here reconstructs it.
  const digest = hashTypedData(noble.keccak_256, typedData);
  const signature = signDigestHex(noble, digest, privateKey);

  const verified = await http("POST", "/v1/principals/verify", {
    body: { nonce, signature },
  });

  const secret = verified?.secret;
  const credential = verified?.credential;
  if (typeof secret !== "string" || secret.length === 0 || !credential) {
    fail(`Verify response carried no credential. Response keys: ${Object.keys(verified ?? {}).join(", ")}`);
  }

  // Written with mode 0600 by saveState. Treat this file as a secret, same as
  // the bearer token: the API shows this value exactly once.
  saveState({
    credential: secret,
    credentialId: credential.credentialId,
    credentialLabel: credential.label,
    credentialScopes: credential.scopes,
    credentialAudience: credential.audience,
    credentialExpiresAt: credential.expiresAt,
  });

  printJson({
    ok: true,
    credentialId: credential.credentialId,
    label: credential.label,
    scopes: credential.scopes,
    audience: credential.audience,
    expiresAt: credential.expiresAt,
    signerAddress,
    stateFile: STATE_FILE,
    note:
      "The credential secret is stored in the state file (mode 0600) and is never printed. It is " +
      "shown by the API exactly once and cannot be read back. Execute calls now send it " +
      "automatically as x-ava-agent-credential. It expires in 15 minutes; run this command again " +
      "before it does (a fresh signature is required — there is no silent refresh).",
  });
}

function help() {
  console.log(`Ava OpenClaw CLI — testnet-first capital tools

Env:
  AVA_API_BASE   default http://127.0.0.1:8787
  AVA_USER_ID    optional; else ~/.config/ava-openclaw/state.json
  AVA_TOKEN      bearer session token; else ~/.config/ava-openclaw/state.json
                 (created by \`session\`, sent as Authorization: Bearer, never printed)
  AVA_AGENT_CREDENTIAL  execute-scoped credential; else ~/.config/ava-openclaw/state.json
                 (created by \`credential\`, sent as x-ava-agent-credential, never printed)
  AVA_SIGNING_KEY_FILE / AVA_SIGNING_KEY_ENV  where \`credential\` reads the signing key
  AVA_PORTAL     default sui
  AVA_ENABLE_LIVE  set true only when live submit is intentionally enabled

Commands:
  health
  session
  tools
  turn "<message>"
  approve [executionId]
  portfolio
  price <asset>
  call <toolName> '<json>'
  credential --key-file <path> | --key-env <ENV_VAR_NAME> [--scopes execute] [--label "..."] [--chain-id 8453]

Canonical loop (NEVER skip user confirm):
  1. session
  2. turn "Swap 10 USDC to SUI on sui with 50 bps slip"
  3. show quote to user → wait for yes
  4. approve <executionId>
  5. portfolio  (before/after proof)

Identity-gated execute paths additionally need a credential:
  credential --key-file ~/.config/ava-openclaw/signer.key   (same key your mandates are signed with)
`);
}

const [cmd, ...rest] = process.argv.slice(2);

async function main() {
  switch (cmd) {
    case "health":
      return cmdHealth();
    case "session":
      return cmdSession();
    case "tools":
      return cmdTools();
    case "turn":
      return cmdTurn(rest.join(" "));
    case "approve":
      return cmdApprove(rest[0]);
    case "portfolio":
      return cmdPortfolio();
    case "price":
      return cmdPrice(rest[0]);
    case "call":
      return cmdCall(rest[0], rest.slice(1).join(" "));
    case "credential":
      return cmdCredential(rest);
    case "help":
    case undefined:
      return help();
    default:
      fail(`Unknown command: ${cmd}\nRun: node scripts/ava.mjs help`);
  }
}

// Runs main() only when this file is the process entry point (`node
// scripts/ava.mjs ...`), not when it is imported as a module (ava.test.mjs
// imports it to test cmdCredential and the EIP-712 helpers directly, against
// a mocked fetch; running the CLI dispatcher as an import side effect would
// make that impossible and would race process.argv against the test runner's
// own).
const isEntryPoint = (() => {
  if (process.argv[1] === undefined) return false;
  try {
    return import.meta.url === pathToFileURL(process.argv[1]).href;
  } catch {
    return false;
  }
})();

if (isEntryPoint) {
  main().catch((e) => {
    console.error(e.message || e);
    process.exit(1);
  });
}

export {
  STATE_DIR,
  STATE_FILE,
  loadState,
  saveState,
  parseFlags,
  readPrivateKey,
  loadNoble,
  addressFromPrivateKey,
  hashTypedData,
  signDigestHex,
  bytesToHex,
  hexToBytes,
  cmdSession,
  cmdTools,
  cmdTurn,
  cmdApprove,
  cmdPortfolio,
  cmdPrice,
  cmdCall,
  cmdHealth,
  cmdCredential,
};
