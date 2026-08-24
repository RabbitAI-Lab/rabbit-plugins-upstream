import { describe, it, before, after } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, statSync, mkdtempSync, writeFileSync, rmSync } from "node:fs";
import { dirname, join } from "node:path";
import { tmpdir } from "node:os";
import { fileURLToPath, pathToFileURL } from "node:url";
import { spawnSync } from "node:child_process";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");

// The CLI resolves its state file from homedir() at module load time, so HOME
// must be redirected to an isolated temp directory BEFORE ava.mjs is
// imported. A test that wrote into the real ~/.config/ava-openclaw would risk
// clobbering a developer's actual session token and credential.
const testHome = mkdtempSync(join(tmpdir(), "ava-openclaw-test-"));
process.env.HOME = testHome;
process.env.USERPROFILE = testHome; // Windows homedir() fallback, harmless elsewhere.

const ava = await import(pathToFileURL(join(root, "scripts/ava.mjs")).href);
// Loaded via a plain relative path (not a declared package.json dependency),
// exactly as the built @ava/tenancy dist is loaded by other packages in this
// workspace. This is the ACTUAL production challenge/verify implementation
// principals.ts calls, used here only to give the CLI's independently
// implemented signer a ground truth to be checked against.
const tenancy = await import(pathToFileURL(join(root, "..", "tenancy", "dist", "index.js")).href);

describe("@ava/openclaw-skill pack", () => {
  it("ships SKILL.md with quote→confirm→approve SOP", () => {
    const skill = readFileSync(join(root, "SKILL.md"), "utf8");
    assert.match(skill, /name:\s*ava/);
    assert.match(skill, /ava_copilot_turn/);
    assert.match(skill, /ava_approve_execute/);
    assert.match(skill, /NEVER/i);
    // The skill must state the honest mode axis. "paper" is banned vocabulary:
    // there is no paper mode on a blockchain, and the word once let a
    // fabricated fill read as a real one.
    assert.match(skill, /testnet/i);
    assert.doesNotMatch(skill, /paper is default/i);
  });

  it("ships catalog with testnet default and tool list", () => {
    const catalog = JSON.parse(readFileSync(join(root, "catalog.json"), "utf8"));
    assert.equal(catalog.defaultMode, "testnet");
    assert.ok(catalog.tools.includes("ava_approve_execute"));
    assert.ok(catalog.tools.includes("ava_copilot_turn"));
  });

  it("CLI exposes canonical commands, including credential", () => {
    const cli = readFileSync(join(root, "scripts/ava.mjs"), "utf8");
    for (const cmd of [
      "cmdSession",
      "cmdTurn",
      "cmdApprove",
      "cmdPortfolio",
      "cmdCredential",
      "ava_approve_execute",
      "ava_copilot_turn",
      "x-ava-agent-credential",
      "principals/challenge",
      "principals/verify",
    ]) {
      assert.ok(cli.includes(cmd), `missing ${cmd}`);
    }
    // The one hard rule of this subcommand: it must never accept the raw key
    // as a flag value. Grepping the source for the refusal is a cheap,
    // permanent guard against someone "simplifying" it back in later.
    assert.match(cli, /Refusing --key/);
  });
});

describe("ava credential (unit, mocked HTTP)", () => {
  const TEST_PRIVATE_KEY_HEX = "59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d".slice(0, 64);
  let noble;
  let signerAddress;
  let keyFilePath;
  let originalFetch;

  before(async () => {
    noble = await ava.loadNoble();
    signerAddress = ava.addressFromPrivateKey(noble, ava.hexToBytes(TEST_PRIVATE_KEY_HEX));
    keyFilePath = join(testHome, "signer.key");
    writeFileSync(keyFilePath, `0x${TEST_PRIVATE_KEY_HEX}\n`, { mode: 0o600 });
    // Preconditions cmdCredential requires before it will even attempt a
    // signature: a stored session (requireUserId / requireToken).
    ava.saveState({ userId: "usr_test_principal", token: "ava_st_test_token" });
    originalFetch = globalThis.fetch;
  });

  after(() => {
    globalThis.fetch = originalFetch;
    rmSync(testHome, { recursive: true, force: true });
  });

  /** A challenge exactly as POST /v1/principals/challenge would construct it. */
  function buildChallenge(overrides = {}) {
    return {
      nonce: "n".repeat(32),
      principalId: "usr_test_principal",
      audience: "ava-openclaw-test",
      chainId: 8453,
      grantLabel: "openclaw-cli on test-host",
      grantScopes: "execute",
      issuedAt: "2026-08-22T12:00:00.000Z",
      expiresAt: "2026-08-22T12:10:00.000Z",
      ...overrides,
    };
  }

  function mockJson(status, body) {
    return new Response(JSON.stringify(body), {
      status,
      headers: { "content-type": "application/json" },
    });
  }

  /**
   * Installs a mock for the two principal endpoints. The verify handler is
   * deliberately dumb — it records what it received and returns a canned
   * success unconditionally — because the cryptographic assertion belongs in
   * the test body, run against the REAL production verifier
   * (`verifyPrincipalChallenge` from @ava/tenancy), not against a mock that
   * could be made to agree with a broken client by construction.
   */
  function installMock({ challenge, signWithOverride } = {}) {
    const c = challenge ?? buildChallenge();
    const typedData = tenancy.principalChallengeTypedData(c);
    const calls = { challenge: 0, verify: 0, verifyBody: undefined };
    globalThis.fetch = async (url, init) => {
      const u = new URL(String(url));
      if (u.pathname === "/v1/principals/challenge" && init?.method === "POST") {
        calls.challenge += 1;
        return mockJson(200, {
          ok: true,
          nonce: c.nonce,
          expiresAt: c.expiresAt,
          typedData,
          signWith: signWithOverride ?? signerAddress,
          nextStep: "Sign this typed data, then POST the nonce and signature to /v1/principals/verify.",
          requestId: "req_test_challenge",
        });
      }
      if (u.pathname === "/v1/principals/verify" && init?.method === "POST") {
        calls.verify += 1;
        calls.verifyBody = JSON.parse(init.body);
        return mockJson(200, {
          ok: true,
          credential: {
            credentialId: "cred_test_1",
            principalId: c.principalId,
            label: c.grantLabel,
            scopes: c.grantScopes.split(","),
            audience: c.audience,
            issuedAt: c.issuedAt,
            expiresAt: c.expiresAt,
          },
          secret: "ava_ac_TOP_SECRET_never_print_this_exact_string",
          proof: { method: "wallet_signature", subject: signerAddress.toLowerCase(), expiresAt: c.expiresAt },
          note: "Store the secret now: it is hashed at rest and cannot be shown again.",
          requestId: "req_test_verify",
        });
      }
      throw new Error(`Unexpected fetch in test: ${init?.method ?? "GET"} ${u.pathname}`);
    };
    return { challenge: c, typedData, calls };
  }

  it("signs exactly the server-provided typed data — the REAL production verifier accepts it", async () => {
    const { challenge, calls } = installMock();
    const logs = [];
    const originalLog = console.log;
    console.log = (...args) => logs.push(args.join(" "));
    try {
      await ava.cmdCredential(["--key-file", keyFilePath, "--label", "test agent", "--scopes", "execute"]);
    } finally {
      console.log = originalLog;
    }

    assert.equal(calls.challenge, 1);
    assert.equal(calls.verify, 1);

    // Exactly {nonce, signature} — anything else would 422 against the real
    // VerifyBodySchema.strict(), so this also guards the wire shape.
    assert.deepEqual(Object.keys(calls.verifyBody).sort(), ["nonce", "signature"]);
    assert.equal(calls.verifyBody.nonce, challenge.nonce);
    assert.match(calls.verifyBody.signature, /^0x[0-9a-f]{130}$/);

    // The load-bearing assertion: hand the captured signature to the ACTUAL
    // server-side verifier (not a reimplementation) against the untouched
    // challenge object. If the CLI's hashTypedData/signDigestHex pipeline had
    // renamed, reordered, dropped, or reconstructed any field instead of
    // hashing exactly what /v1/principals/challenge returned, this recovers
    // the wrong address (or fails outright) rather than the test's own key.
    const verdict = tenancy.verifyPrincipalChallenge({
      challenge,
      signature: calls.verifyBody.signature,
      expectedSigner: signerAddress,
      principalId: challenge.principalId,
      audience: challenge.audience,
      now: new Date("2026-08-22T12:01:00.000Z"),
      proofTtlMs: 10 * 60 * 1000,
    });
    assert.equal(verdict.ok, true, `expected the real verifier to accept the signature, got: ${JSON.stringify(verdict)}`);
    assert.equal(verdict.signerAddress, signerAddress.toLowerCase());

    const printed = logs.join("\n");
    assert.doesNotMatch(printed, /ava_ac_TOP_SECRET_never_print_this_exact_string/);
  });

  it("stores the credential secret in state.json at mode 0600, and it is never written to stdout", async () => {
    installMock();
    const logs = [];
    const originalLog = console.log;
    console.log = (...args) => logs.push(args.join(" "));
    try {
      await ava.cmdCredential(["--key-file", keyFilePath]);
    } finally {
      console.log = originalLog;
    }

    const state = JSON.parse(readFileSync(ava.STATE_FILE, "utf8"));
    assert.equal(state.credential, "ava_ac_TOP_SECRET_never_print_this_exact_string");
    assert.equal(state.credentialId, "cred_test_1");
    assert.deepEqual(state.credentialScopes, ["execute"]);

    const mode = statSync(ava.STATE_FILE).mode & 0o777;
    assert.equal(mode, 0o600, `expected state file mode 0600, got ${mode.toString(8)}`);

    const printed = logs.join("\n");
    assert.doesNotMatch(printed, /ava_ac_TOP_SECRET_never_print_this_exact_string/);
    // The printed summary is expected to carry the metadata a caller needs —
    // proving this is not decoration by also asserting the positive shape.
    assert.match(printed, /"credentialId": "cred_test_1"/);
    assert.match(printed, /"scopes": \[\s*"execute"\s*\]/);
  });

  it("attaches the stored credential as x-ava-agent-credential on later authenticated calls, mirroring the bearer", async () => {
    installMock();
    const originalLogSetup = console.log;
    console.log = () => {};
    try {
      await ava.cmdCredential(["--key-file", keyFilePath]);
    } finally {
      console.log = originalLogSetup;
    }

    // cmdTools deliberately calls http() with `auth: false` (tool listing
    // needs no session), so it must NOT be the one carrying either header —
    // asserting that first is what makes the authenticated-call assertion
    // below meaningful rather than "every outgoing request always gets it".
    let toolsCallHeaders;
    globalThis.fetch = async (url, init) => {
      toolsCallHeaders = init?.headers ?? {};
      return mockJson(200, { ok: true, tools: [], server: { name: "ava" } });
    };
    const originalLogTools = console.log;
    console.log = () => {};
    try {
      await ava.cmdTools();
    } finally {
      console.log = originalLogTools;
    }
    assert.equal(toolsCallHeaders["x-ava-agent-credential"], undefined);
    assert.equal(toolsCallHeaders.authorization, undefined);

    // cmdPortfolio requires a session (auth: true) and is exactly the kind of
    // call an execute-gated route reads the credential from.
    let seenHeader;
    let seenBearer;
    globalThis.fetch = async (url, init) => {
      seenHeader = init?.headers?.["x-ava-agent-credential"];
      seenBearer = init?.headers?.authorization;
      return mockJson(200, { ok: true, result: { structuredContent: { balances: [] } } });
    };
    const originalLogPortfolio = console.log;
    console.log = () => {};
    try {
      await ava.cmdPortfolio();
    } finally {
      console.log = originalLogPortfolio;
    }
    assert.equal(seenHeader, "ava_ac_TOP_SECRET_never_print_this_exact_string");
    assert.equal(seenBearer, "Bearer ava_st_test_token");
  });

  it("refuses when the local key does not match the address Ava expects (client-side pre-check)", async () => {
    installMock({ signWithOverride: "0x000000000000000000000000000000deadbeef" });
    let exitCode;
    const originalExit = process.exit;
    const errors = [];
    const originalError = console.error;
    process.exit = (code) => {
      exitCode = code;
      throw new Error("__test_process_exit__");
    };
    console.error = (...args) => errors.push(args.join(" "));
    try {
      await ava.cmdCredential(["--key-file", keyFilePath]);
      assert.fail("expected cmdCredential to refuse a signer mismatch");
    } catch (e) {
      assert.equal(e.message, "__test_process_exit__");
    } finally {
      process.exit = originalExit;
      console.error = originalError;
    }
    assert.equal(exitCode, 1);
    assert.match(errors.join("\n"), /does not match|expects the address/i);
  });

  it("REFUSES a raw --key on argv without ever touching the network (subprocess)", () => {
    const result = spawnSync(
      process.execPath,
      [join(root, "scripts/ava.mjs"), "credential", "--key", "deadbeef".repeat(8)],
      { encoding: "utf8", env: { ...process.env, HOME: testHome, AVA_API_BASE: "http://127.0.0.1:1" } },
    );
    assert.equal(result.status, 1);
    assert.match(result.stderr, /Refusing --key/);
  });

  it("REFUSES when neither --key-file nor --key-env is given (subprocess)", () => {
    const result = spawnSync(
      process.execPath,
      [join(root, "scripts/ava.mjs"), "credential"],
      {
        encoding: "utf8",
        env: {
          ...process.env,
          HOME: testHome,
          AVA_SIGNING_KEY_FILE: "",
          AVA_SIGNING_KEY_ENV: "",
          AVA_API_BASE: "http://127.0.0.1:1",
        },
      },
    );
    assert.equal(result.status, 1);
    assert.match(result.stderr, /--key-file/);
  });
});

describe("EIP-712 typed-data hashing — mutation coverage", () => {
  it("changes digest when any signed field changes (nonce, scopes, label)", async () => {
    const noble = await ava.loadNoble();
    const base = tenancy.principalChallengeTypedData({
      nonce: "n".repeat(32),
      principalId: "usr_a",
      audience: "ava-test",
      chainId: 8453,
      grantLabel: "agent-a",
      grantScopes: "execute",
      issuedAt: "2026-08-22T00:00:00.000Z",
      expiresAt: "2026-08-22T00:10:00.000Z",
    });
    const scopesEscalated = tenancy.principalChallengeTypedData({
      nonce: "n".repeat(32),
      principalId: "usr_a",
      audience: "ava-test",
      chainId: 8453,
      grantLabel: "agent-a",
      grantScopes: "execute,mandate_admin",
      issuedAt: "2026-08-22T00:00:00.000Z",
      expiresAt: "2026-08-22T00:10:00.000Z",
    });

    const d1 = ava.hashTypedData(noble.keccak_256, base);
    const d2 = ava.hashTypedData(noble.keccak_256, scopesEscalated);
    assert.notEqual(d1, d2, "a wider scope grant must not hash to the same digest as the narrower one");
  });

  it("matches @ava/tenancy's own digest bit-for-bit (cross-check against production)", async () => {
    const noble = await ava.loadNoble();
    const challenge = {
      nonce: "z".repeat(32),
      principalId: "usr_cross_check",
      audience: "ava-production",
      chainId: 1,
      grantLabel: "cross-check agent",
      grantScopes: "execute,read",
      issuedAt: "2026-01-01T00:00:00.000Z",
      expiresAt: "2026-01-01T00:05:00.000Z",
    };
    const typedData = tenancy.principalChallengeTypedData(challenge);
    const cliDigest = ava.hashTypedData(noble.keccak_256, typedData);
    const realDigest = tenancy.principalChallengeDigest(challenge);
    assert.equal(cliDigest, realDigest);
  });
});
