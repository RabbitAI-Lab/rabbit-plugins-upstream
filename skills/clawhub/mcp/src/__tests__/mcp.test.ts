import { spawn } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { afterEach, describe, expect, it } from 'vitest';
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { InMemoryTransport } from '@modelcontextprotocol/sdk/inMemory.js';
import {
  createPublicClient,
  decodeFunctionData,
  encodeAbiParameters,
  encodeEventTopics,
  http,
  keccak256,
  parseAbiParameters,
  stringToHex,
  type Address,
  type Hex,
  type PublicClient,
} from 'viem';
import { base } from 'viem/chains';
import { privateKeyToAccount } from 'viem/accounts';
import {
  CANONICAL_VAULT_V33_ADDRESS,
  CBBTC_BASE_ADDRESS,
  CRYPTO_SLIP_VAULT_V32_ABI,
  RelayGatewayClient,
  USDC_BASE_ADDRESS,
  ZERO_ADDRESS,
  encodeSlipUrl,
  grossUpForExactNet,
  type UserOpCall,
} from '@cryptoslip/sdk';
import { PocketSlipVault } from '../pocketSlip.js';
import { CRYPTOSLIP_MCP_TOOL_NAMES, createCryptoSlipMcpServer } from '../server.js';

const deriveKey = (label: string): Hex => keccak256(stringToHex(label));

interface SimulatedSlipRow {
  slipId: bigint;
  asset: Address;
  amount: bigint;
  createdAt: number;
  cancelLockedUntil: bigint;
  creator: Address;
  claimSigner: Address;
  refundBeneficiary: Address;
  refundFeeRequired: boolean;
  nonce: bigint;
  status: number;
}

function createSimulatedBaseEnvironment(initialSlips: SimulatedSlipRow[]) {
  const slips = new Map<string, SimulatedSlipRow>();
  let nextSlipId = 500n;
  const broadcastedCalls: UserOpCall[] = [];
  const receipts = new Map<Hex, { logs: Array<{ address: Address; topics: Hex[]; data: Hex }> }>();

  for (const s of initialSlips) {
    slips.set(s.slipId.toString(), { ...s });
    if (s.slipId >= nextSlipId) nextSlipId = s.slipId + 1n;
  }

  const directBroadcast = async (call: UserOpCall): Promise<Hex> => {
    broadcastedCalls.push(call);
    const txHash = keccak256(stringToHex(`sim-tx-${broadcastedCalls.length}-${call.data.slice(0, 40)}`));
    const decoded = decodeFunctionData({
      abi: CRYPTO_SLIP_VAULT_V32_ABI,
      data: call.data,
    });

    if (decoded.functionName === 'acceptWithPermit') {
      const [slipId, , newClaimSigner, keepEscrowedInVault] = decoded.args;
      const row = slips.get(slipId.toString());
      if (!row || row.status !== 1) throw new Error('InvalidSlipStatus');
      row.claimSigner = newClaimSigner;
      row.nonce += 1n;
      if (keepEscrowedInVault) {
        row.refundFeeRequired = true;
      }
      receipts.set(txHash, { logs: [] });
      return txHash;
    }

    if (decoded.functionName === 'splitAndPayWithPermit') {
      const [slipId, paymentAmount, merchant, changeReceiver, newChangeSigner] = decoded.args;
      const row = slips.get(slipId.toString());
      if (!row || row.status !== 1) throw new Error('InvalidSlipStatus');
      row.status = 4; // SPLIT
      row.nonce += 1n;

      const changeAmount = row.amount - paymentAmount;
      let changeSlipId = 0n;
      if (changeAmount > 0n && changeReceiver.toLowerCase() === CANONICAL_VAULT_V33_ADDRESS.toLowerCase()) {
        changeSlipId = nextSlipId++;
        slips.set(changeSlipId.toString(), {
          slipId: changeSlipId,
          asset: row.asset,
          amount: changeAmount,
          createdAt: 1_795_000_000,
          cancelLockedUntil: row.cancelLockedUntil,
          creator: row.creator,
          claimSigner: newChangeSigner,
          refundBeneficiary: newChangeSigner,
          refundFeeRequired: true,
          nonce: 0n,
          status: 1,
        });
      }

      const topics = encodeEventTopics({
        abi: CRYPTO_SLIP_VAULT_V32_ABI,
        eventName: 'SlipSplitAndPaid',
        args: {
          originalSlipId: slipId,
          changeSlipId,
          merchant,
        },
      });
      const data = encodeAbiParameters(parseAbiParameters('uint256, uint256'), [
        paymentAmount,
        changeAmount,
      ]);

      receipts.set(txHash, {
        logs: [
          {
            address: CANONICAL_VAULT_V33_ADDRESS,
            topics: topics as Hex[],
            data,
          },
        ],
      });
      return txHash;
    }

    receipts.set(txHash, { logs: [] });
    return txHash;
  };

  const mockPublicClient = {
    getBlock: async () => ({ timestamp: 1_795_000_100n, number: 28_500_000n }),
    getCode: async () => '0x',
    readContract: async (args: {
      address: Address;
      functionName: string;
      args?: readonly unknown[];
    }) => {
      const idStr = args.args?.[0] !== undefined ? String(args.args[0]) : '';
      const row = slips.get(idStr);
      if (args.functionName === 'slips') {
        if (!row) {
          return [ZERO_ADDRESS, 0n, 0, 0, ZERO_ADDRESS, ZERO_ADDRESS, 0] as const;
        }
        return [
          row.asset,
          row.amount,
          row.createdAt,
          Number(row.cancelLockedUntil),
          row.creator,
          row.claimSigner,
          row.status,
        ] as const;
      }
      if (args.functionName === 'nonces') {
        return row ? row.nonce : 0n;
      }
      if (args.functionName === 'refundBeneficiary') {
        return row ? row.refundBeneficiary : ZERO_ADDRESS;
      }
      if (args.functionName === 'refundFeeRequired') {
        return row ? row.refundFeeRequired : false;
      }
      if (args.functionName === 'referralCredits') {
        return 0n;
      }
      if (args.functionName === 'totalSlips') {
        return nextSlipId - 1n;
      }
      if (args.functionName === 'balanceOf') {
        return 0n;
      }
      throw new Error(`Unhandled readContract: ${args.functionName}`);
    },
    waitForTransactionReceipt: async ({ hash }: { hash: Hex }) => {
      const rec = receipts.get(hash) ?? { logs: [] };
      return {
        status: 'success',
        transactionHash: hash,
        blockNumber: 28_500_001n,
        logs: rec.logs,
      };
    },
  } as unknown as PublicClient;

  const offlineRelayClient = new RelayGatewayClient({
    fetchFn: async () => new Response('simulated offline relay', { status: 503 }),
  });

  return { slips, broadcastedCalls, directBroadcast, offlineRelayClient, mockPublicClient };
}

describe('@cryptoslip/mcp PocketSlipVault & MCP Stdio Server (V-01..V-04)', () => {
  const tempDirs: string[] = [];

  afterEach(() => {
    for (const dir of tempDirs.splice(0)) {
      fs.rmSync(dir, { recursive: true, force: true });
    }
  });

  it('V-01: bootAndRotate() immediately rotates an unrotated .env slip via 0%-fee Keep, persists 0600 state, and scrubs secrets', async () => {
    const creator = privateKeyToAccount(deriveKey('mcp-creator-1')).address;
    const initialClaimKey = deriveKey('mcp-initial-env-slip-key-1');
    const initialClaimAddr = privateKeyToAccount(initialClaimKey).address;

    const { slips, broadcastedCalls, directBroadcast, offlineRelayClient, mockPublicClient } =
      createSimulatedBaseEnvironment([
        {
          slipId: 101n,
          asset: USDC_BASE_ADDRESS,
          amount: 5_000_000n, // $5.00 USDC
          createdAt: 1_795_000_000,
          cancelLockedUntil: 0n,
          creator,
          claimSigner: initialClaimAddr,
          refundBeneficiary: creator,
          refundFeeRequired: false,
          nonce: 0n,
          status: 1,
        },
      ]);

    const { webUrl } = encodeSlipUrl({
      id: '101',
      amount: 5,
      asset: 'USDC',
      vault: 'v33',
      mode: 'open',
      claimKey: initialClaimKey,
    });

    const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'pocket-slip-v01-'));
    tempDirs.push(tmpDir);
    const stateFilePath = path.join(tmpDir, 'pocket-state.json');

    const pocket = new PocketSlipVault({
      slipUrl: webUrl,
      stateFilePath,
      publicClient: mockPublicClient,
      transportOverrides: { directBroadcast, relayClient: offlineRelayClient },
    });

    const bootRes = await pocket.bootAndRotate();
    expect(bootRes).not.toBeNull();
    expect(bootRes?.bootRotated).toBe(true);
    expect(bootRes?.balanceUnits).toBe('5000000'); // 0% 1st Keep fee!
    expect(bootRes?.activeClaimSigner.toLowerCase()).not.toBe(initialClaimAddr.toLowerCase());
    expect(broadcastedCalls.length).toBe(1);

    // Original .env link is now invalidated on-chain!
    expect(slips.get('101')?.claimSigner.toLowerCase()).toBe(
      bootRes?.activeClaimSigner.toLowerCase(),
    );
    expect(slips.get('101')?.nonce).toBe(1n);

    // Persisted local state exists and resumes without a second Keep on restart
    expect(fs.existsSync(stateFilePath)).toBe(true);
    const persistedJson = JSON.parse(fs.readFileSync(stateFilePath, 'utf8')) as {
      activeClaimPrivateKey: string;
    };
    expect(persistedJson.activeClaimPrivateKey).toMatch(/^0x[0-9a-fA-F]{64}$/);

    const restartedPocket = new PocketSlipVault({
      slipUrl: webUrl,
      stateFilePath,
      publicClient: mockPublicClient,
      transportOverrides: { directBroadcast, relayClient: offlineRelayClient },
    });
    const resumeRes = await restartedPocket.bootAndRotate();
    expect(resumeRes?.bootRotated).toBe(false);
    expect(resumeRes?.resumedFromLocalState).toBe(true);
    expect(broadcastedCalls.length).toBe(1); // Zero extra tx on restart!

    // Status output scrubs ALL raw 64-hex private keys
    const status = await restartedPocket.getStatus();
    const statusJson = JSON.stringify(status);
    expect(statusJson).not.toContain(initialClaimKey.slice(2));
    expect(statusJson).not.toContain(persistedJson.activeClaimPrivateKey.slice(2));
    expect(status.balanceUnits).toBe('5000000');
  });

  it('V-02 / V-03 / V-04: MCP tools enforce spend caps, rate limits, blocked destinations, domain allowlists, and $0.10 dust guard', async () => {
    const creator = privateKeyToAccount(deriveKey('mcp-creator-2')).address;
    const initialClaimKey = deriveKey('mcp-initial-env-slip-key-2');
    const initialClaimAddr = privateKeyToAccount(initialClaimKey).address;
    const validMerchant = privateKeyToAccount(deriveKey('mcp-valid-merchant-2')).address;

    const { broadcastedCalls, directBroadcast, offlineRelayClient, mockPublicClient } = createSimulatedBaseEnvironment([
      {
        slipId: 202n,
        asset: USDC_BASE_ADDRESS,
        amount: 500_000n, // $0.50 USDC slip to also test $0.05 dust cliff!
        createdAt: 1_795_000_000,
        cancelLockedUntil: 0n,
        creator,
        claimSigner: initialClaimAddr,
        refundBeneficiary: creator,
        refundFeeRequired: false,
        nonce: 0n,
        status: 1,
      },
    ]);

    const { webUrl } = encodeSlipUrl({
      id: '202',
      amount: 0.5,
      asset: 'USDC',
      vault: 'v33',
      mode: 'open',
      claimKey: initialClaimKey,
    });

    const pocket = new PocketSlipVault({
      slipUrl: webUrl,
      stateFilePath: null,
      publicClient: mockPublicClient,
      policy: {
        maxPerCallUsdMicro: 450_000n, // $0.45 cap
        maxDailyUsdMicro: 2_000_000n,
        maxSpendsPerMinute: 2,
        allowedDomains: ['api.trusted-compute.io'],
      },
      transportOverrides: { directBroadcast, relayClient: offlineRelayClient },
    });

    const { server } = createCryptoSlipMcpServer({ vault: pocket });
    const [clientTransport, serverTransport] = InMemoryTransport.createLinkedPair();
    const client = new Client({ name: 'mcp-test-client', version: '1.0.0' });

    await Promise.all([server.connect(serverTransport), client.connect(clientTransport)]);

    const listed = await client.listTools();
    const listedNames = listed.tools.map((t) => t.name);
    expect(listedNames).toEqual([...CRYPTOSLIP_MCP_TOOL_NAMES]);

    // 1. Prompt-injection over-cap ($0.50 > $0.45 cap) is deterministically rejected
    const overCap = await client.callTool({
      name: 'cryptoslip_pay_x402_or_merchant',
      arguments: {
        recipient: validMerchant,
        amount: '0.50',
      },
    });
    expect(overCap.isError).toBe(true);
    expect(JSON.stringify(overCap.content)).toContain('SPEND_CAP_EXCEEDED');

    // 2. Blocked destination (0x...dEaD and v33 Vault) is rejected
    const deadDest = await client.callTool({
      name: 'cryptoslip_pay_x402_or_merchant',
      arguments: {
        recipient: '0x000000000000000000000000000000000000dEaD',
        amount: '0.15',
      },
    });
    expect(deadDest.isError).toBe(true);
    expect(JSON.stringify(deadDest.content)).toContain('BLOCKED_DESTINATION');

    // 3. Untrusted HTTP 402 domain is rejected
    const badDomain = await client.callTool({
      name: 'cryptoslip_pay_x402_or_merchant',
      arguments: {
        recipient: validMerchant,
        amount: '0.15',
        endpointUrl: 'https://evil-drain.example.org/x402',
      },
    });
    expect(badDomain.isError).toBe(true);
    expect(JSON.stringify(badDomain.content)).toContain('DOMAIN_NOT_ALLOWLISTED');

    // 4. V-03 Dust cliff ($0.50 slip - $0.44 payment = $0.06 remainder < $0.10 minSlipAmount) is rejected!
    const dustCliff = await client.callTool({
      name: 'cryptoslip_pay_x402_or_merchant',
      arguments: {
        recipient: validMerchant,
        amount: '0.44',
        endpointUrl: 'https://api.trusted-compute.io/v1/run',
      },
    });
    expect(dustCliff.isError).toBe(true);
    expect(JSON.stringify(dustCliff.content)).toContain('DustCliffError');

    // 5. Valid $0.20 spend #1 succeeds ($0.30 remaining >= $0.10)
    const spend1 = await client.callTool({
      name: 'cryptoslip_pay_x402_or_merchant',
      arguments: {
        recipient: validMerchant,
        amount: '0.20',
        endpointUrl: 'https://api.trusted-compute.io/v1/run',
      },
    });
    expect(spend1.isError).toBeFalsy();
    const spend1Data = JSON.parse((spend1.content as Array<{ text: string }>)[0]!.text) as {
      remainingChangeUnits: string;
      newActiveSlipId: string;
    };
    expect(spend1Data.remainingChangeUnits).toBe('300000');
    expect(spend1Data.newActiveSlipId).toBe('500');

    // 6. Valid $0.15 spend #2 succeeds ($0.15 remaining >= $0.10)
    const spend2 = await client.callTool({
      name: 'cryptoslip_pay_x402_or_merchant',
      arguments: {
        recipient: validMerchant,
        amount: '0.15',
        endpointUrl: 'https://api.trusted-compute.io/v1/run',
      },
    });
    expect(spend2.isError).toBeFalsy();

    // 7. Spend #3 within same 60s window hits sliding rate limit (2/min)!
    const txCountBeforeRateLimit = broadcastedCalls.length;
    const spend3 = await client.callTool({
      name: 'cryptoslip_pay_x402_or_merchant',
      arguments: {
        recipient: validMerchant,
        amount: '0.15',
        endpointUrl: 'https://api.trusted-compute.io/v1/run',
      },
    });
    expect(spend3.isError).toBe(true);
    expect(JSON.stringify(spend3.content)).toContain('RATE_LIMIT_EXCEEDED');
    expect(broadcastedCalls.length).toBe(txCountBeforeRateLimit);

    await client.close();
    await server.close();
  });

  it('supports cryptoslip_pay_human outbound DM policy, signed receipt export, and stdio CLI tools/list', async () => {
    const recipient = privateKeyToAccount(deriveKey('mcp-receipt-recipient')).address;
    const dummyClaimKey = deriveKey('mcp-human-bounty-key');
    const { webUrl: mockedMintedUrl } = encodeSlipUrl({
      id: '901',
      amount: 1.25,
      asset: 'USDC',
      vault: 'v33',
      mode: 'open',
      claimKey: dummyClaimKey,
      cancelLockedUntil: 9_999_999_999,
    });
    const mockTxHash = keccak256(stringToHex('mcp-human-mint-tx'));

    const pocket = new PocketSlipVault({
      stateFilePath: null,
      policy: {
        maxPerCallUsdMicro: 5_000_000n,
        maxDailyUsdMicro: 20_000_000n,
        allowOutboundSlipLinks: true,
      },
      customBatchExecutor: async () => ({
        prepared: {} as never,
        txHashes: [mockTxHash],
        mintedSlips: [
          {
            index: 0,
            slipId: '901',
            txHash: mockTxHash,
            blockNumber: 28_500_010,
            vault: 'v33',
            vaultAddress: CANONICAL_VAULT_V33_ADDRESS,
            creator: recipient,
            asset: 'USDC',
            grossAmountUnits: '1250000',
            guaranteedNetClaimUnits: '1243750',
            humanAmount: 1.25,
            mode: 'open',
            cancelLockedUntil: 9_999_999_999,
            claimSigner: privateKeyToAccount(dummyClaimKey).address,
            payload: 'slip_901',
            url: mockedMintedUrl,
            sovereignUrl: mockedMintedUrl,
            telegramUrl: null,
          },
        ],
        csv: 'index,url\n0,' + mockedMintedUrl,
        json: '[]',
      }),
    });

    const humanRes = await pocket.payHuman({
      amount: '1.25',
      asset: 'USDC',
      noTakeBack: true,
    });
    expect(humanRes.outboundSlipUrl).toBe(mockedMintedUrl);
    expect(humanRes.noTakeBack).toBe(true);

    // Export signed receipt + printable Green-Zone HTML
    const receiptExport = await pocket.verifyOrExportReceipt({
      action: 'export',
      receiptInput: {
        slipId: '901',
        txHash: mockTxHash,
        blockNumber: 28_500_010,
        blockTimestamp: 1_795_000_200,
        settlementType: 'mint',
        asset: 'USDC',
        grossAmount: '1250000',
        feeAmount: '0',
        netAmount: '1250000',
        recipient,
        merchantLabel: 'Agent Bounty',
      },
      signWithOperatorKey: true,
      includeCsv: true,
      includeHtml: true,
    });
    expect(receiptExport.action).toBe('export');
    expect(typeof receiptExport.html).toBe('string');
    expect(typeof receiptExport.csvRow).toBe('string');

    // Verify Markdown docs obey AGENTS.md Rule #3 Legal Green-Zone forbidden red-zone words
    const testDir = path.dirname(fileURLToPath(import.meta.url));
    const mcpRoot = path.resolve(testDir, '../..');
    const sdkRoot = path.resolve(mcpRoot, '../sdk');
    const docPaths = [
      path.join(sdkRoot, 'README.md'),
      path.join(mcpRoot, 'README.md'),
      path.join(mcpRoot, 'SKILL.md'),
    ];
    const forbiddenRe =
      /\b(?:digital\s+cash|dollars?|crypto\s+bank|deposit|interest|yield|apy|mixer|tornado|fdic|escrow|bearer|expires\s+in)\b/i;
    for (const docPath of docPaths) {
      const content = fs.readFileSync(docPath, 'utf8');
      expect(content).not.toMatch(forbiddenRe);
    }

    // Spawn compiled CLI over stdio if dist/cli.js exists (built before/during CI gate)
    const cliDistPath = path.join(mcpRoot, 'dist', 'cli.js');
    if (fs.existsSync(cliDistPath)) {
      const stdoutLines = await new Promise<string[]>((resolve, reject) => {
        const child = spawn(process.execPath, [cliDistPath], {
          stdio: ['pipe', 'pipe', 'pipe'],
          env: { ...process.env, CRYPTOSLIP_URL: '' },
        });
        const lines: string[] = [];
        let buf = '';
        child.stdout.setEncoding('utf8');
        let settled = false;
        const timer = setTimeout(() => {
          if (settled) return;
          settled = true;
          child.kill();
          resolve(lines);
        }, 20_000);
        child.stdout.on('data', (chunk: string) => {
          buf += chunk;
          const parts = buf.split('\n');
          buf = parts.pop() ?? '';
          for (const p of parts) {
            if (p.trim()) lines.push(p.trim());
          }
          if (lines.length >= 2 && !settled) {
            settled = true;
            clearTimeout(timer);
            child.kill();
            resolve(lines);
          }
        });
        child.on('error', (err) => {
          clearTimeout(timer);
          if (!settled) {
            settled = true;
            reject(err);
          }
        });

        child.stdin.write(
          JSON.stringify({
            jsonrpc: '2.0',
            id: 1,
            method: 'initialize',
            params: {
              protocolVersion: '2024-11-05',
              capabilities: {},
              clientInfo: { name: 'smoke', version: '1.0.0' },
            },
          }) + '\n',
        );
        child.stdin.write(
          JSON.stringify({
            jsonrpc: '2.0',
            method: 'notifications/initialized',
          }) + '\n',
        );
        child.stdin.write(
          JSON.stringify({
            jsonrpc: '2.0',
            id: 2,
            method: 'tools/list',
            params: {},
          }) + '\n',
        );
      });

      expect(stdoutLines.length).toBeGreaterThanOrEqual(2);
      const listFrame = JSON.parse(stdoutLines[1]!) as {
        result?: { tools?: Array<{ name: string }> };
      };
      expect(listFrame.result?.tools?.map((t) => t.name)).toEqual([
        ...CRYPTOSLIP_MCP_TOOL_NAMES,
      ]);
    }
  }, 30_000);

  it('exercises cryptoslip_batch_payout, cryptoslip_reclaim_unclaimed, and cryptoslip_withdraw_referrals via MCP client', async () => {
    const mockTxHash = keccak256(stringToHex('mcp-batch-tx-1'));
    const batchKey1 = deriveKey('mcp-batch-link-1');
    const batchKey2 = deriveKey('mcp-batch-link-2');
    const { webUrl: url1 } = encodeSlipUrl({
      id: '701',
      amount: 0.25,
      asset: 'USDC',
      vault: 'v33',
      mode: 'open',
      claimKey: batchKey1,
    });
    const { webUrl: url2 } = encodeSlipUrl({
      id: '702',
      amount: 0.25,
      asset: 'USDC',
      vault: 'v33',
      mode: 'open',
      claimKey: batchKey2,
    });

    const { mockPublicClient, offlineRelayClient, directBroadcast } =
      createSimulatedBaseEnvironment([]);

    const pocket = new PocketSlipVault({
      stateFilePath: null,
      publicClient: mockPublicClient,
      policy: {
        maxPerCallUsdMicro: 2_000_000n,
        maxDailyUsdMicro: 10_000_000n,
      },
      transportOverrides: { relayClient: offlineRelayClient, directBroadcast },
      customBatchExecutor: async () => ({
        prepared: {} as never,
        txHashes: [mockTxHash],
        mintedSlips: [
          {
            index: 0,
            slipId: '701',
            txHash: mockTxHash,
            blockNumber: 28_500_020,
            vault: 'v33',
            vaultAddress: CANONICAL_VAULT_V33_ADDRESS,
            creator: privateKeyToAccount(deriveKey('mcp-op')).address,
            asset: 'USDC',
            grossAmountUnits: '250000',
            guaranteedNetClaimUnits: '248750',
            humanAmount: 0.25,
            mode: 'open',
            cancelLockedUntil: 0,
            claimSigner: privateKeyToAccount(batchKey1).address,
            payload: 'slip_701',
            url: url1,
            sovereignUrl: url1,
            telegramUrl: null,
          },
          {
            index: 1,
            slipId: '702',
            txHash: mockTxHash,
            blockNumber: 28_500_020,
            vault: 'v33',
            vaultAddress: CANONICAL_VAULT_V33_ADDRESS,
            creator: privateKeyToAccount(deriveKey('mcp-op')).address,
            asset: 'USDC',
            grossAmountUnits: '250000',
            guaranteedNetClaimUnits: '248750',
            humanAmount: 0.25,
            mode: 'open',
            cancelLockedUntil: 0,
            claimSigner: privateKeyToAccount(batchKey2).address,
            payload: 'slip_702',
            url: url2,
            sovereignUrl: url2,
            telegramUrl: null,
          },
        ],
        csv: `index,url\n0,${url1}\n1,${url2}`,
        json: '[]',
      }),
    });

    const { server } = createCryptoSlipMcpServer({ vault: pocket });
    const [clientTransport, serverTransport] = InMemoryTransport.createLinkedPair();
    const client = new Client({ name: 'mcp-full-tools-client', version: '1.0.0' });
    await Promise.all([server.connect(serverTransport), client.connect(clientTransport)]);

    const batchRes = await client.callTool({
      name: 'cryptoslip_batch_payout',
      arguments: {
        items: [
          { amount: '0.25', asset: 'USDC', recipientRef: '@alice' },
          { amount: '0.25', asset: 'USDC', recipientRef: '@bob' },
        ],
        format: 'both',
      },
    });
    expect(batchRes.isError).toBeFalsy();
    const batchData = JSON.parse((batchRes.content as Array<{ text: string }>)[0]!.text) as {
      count: number;
      outboundLinks: Array<{ url: string }>;
      outboundCsv: string;
    };
    expect(batchData.count).toBe(2);
    expect(batchData.outboundLinks[0]?.url).toBe(url1);
    expect(batchData.outboundCsv).toContain(url2);

    const scanRes = await client.callTool({
      name: 'cryptoslip_reclaim_unclaimed',
      arguments: { scanOnly: true },
    });
    expect(scanRes.isError).toBeFalsy();

    const refRes = await client.callTool({
      name: 'cryptoslip_withdraw_referrals',
      arguments: { assets: ['USDC', 'NARA'] },
    });
    expect(refRes.isError).toBeFalsy();

    // Blocked destination on referral withdrawal is caught by policy
    const badRefDest = await client.callTool({
      name: 'cryptoslip_withdraw_referrals',
      arguments: { to: '0x000000000000000000000000000000000000dEaD' },
    });
    expect(badRefDest.isError).toBe(true);
    expect(JSON.stringify(badRefDest.content)).toContain('BLOCKED_DESTINATION');

    await client.close();
    await server.close();
  });

  it('3R regressions: handles ETH & cbBTC PocketSlips accurately and funds $0.10 Circle Paymaster headroom on payHuman with allowedRecipients', async () => {
    const creator = privateKeyToAccount(deriveKey('mcp-3r-creator')).address;
    const ethKey = deriveKey('mcp-3r-eth-slip');
    const btcKey = deriveKey('mcp-3r-btc-slip');
    const usdcKey = deriveKey('mcp-3r-usdc-slip');
    const allowedMerchant = privateKeyToAccount(deriveKey('mcp-3r-allowed-merchant')).address;

    const { broadcastedCalls, directBroadcast, offlineRelayClient, mockPublicClient } =
      createSimulatedBaseEnvironment([
        {
          slipId: 301n,
          asset: ZERO_ADDRESS, // ETH (18 decimals, $2,500/ETH)
          amount: 2_000_000_000_000_000n, // 0.002 ETH = $5.00
          createdAt: 1_795_000_000,
          cancelLockedUntil: 0n,
          creator,
          claimSigner: privateKeyToAccount(ethKey).address,
          refundBeneficiary: creator,
          refundFeeRequired: false,
          nonce: 0n,
          status: 1,
        },
        {
          slipId: 302n,
          asset: CBBTC_BASE_ADDRESS, // cbBTC (8 decimals, $50,000/BTC)
          amount: 1_000_000n, // 0.01 BTC = $500.00
          createdAt: 1_795_000_000,
          cancelLockedUntil: 0n,
          creator,
          claimSigner: privateKeyToAccount(btcKey).address,
          refundBeneficiary: creator,
          refundFeeRequired: false,
          nonce: 0n,
          status: 1,
        },
        {
          slipId: 303n,
          asset: USDC_BASE_ADDRESS,
          amount: 5_000_000n, // $5.00 USDC
          createdAt: 1_795_000_000,
          cancelLockedUntil: 0n,
          creator,
          claimSigner: privateKeyToAccount(usdcKey).address,
          refundBeneficiary: creator,
          refundFeeRequired: false,
          nonce: 0n,
          status: 1,
        },
      ]);

    // 1. ETH PocketSlip: 0.0001 ETH ($0.25) spend succeeds under $0.50 cap without false $100M DoS
    const ethSlipUrl = encodeSlipUrl({
      id: '301',
      amount: 0.002,
      asset: 'ETH',
      vault: 'v33',
      mode: 'open',
      claimKey: ethKey,
    }).webUrl;
    const ethPocket = new PocketSlipVault({
      slipUrl: ethSlipUrl,
      stateFilePath: null,
      publicClient: mockPublicClient,
      policy: { maxPerCallUsdMicro: 500_000n, maxDailyUsdMicro: 5_000_000n },
      transportOverrides: { directBroadcast, relayClient: offlineRelayClient },
    });
    const ethSpend = await ethPocket.payMerchantOrX402({
      recipient: allowedMerchant,
      amount: '0.0001',
    });
    expect(ethSpend.asset).toBe('ETH');
    expect(ethSpend.grossPaymentUnits).toBe('100000000000000');

    // 2. cbBTC PocketSlip: 0.005 BTC (500,000 sats = $250.00) MUST be blocked under $0.50 cap!
    const btcSlipUrl = encodeSlipUrl({
      id: '302',
      amount: 0.01,
      asset: 'BTC',
      vault: 'v33',
      mode: 'open',
      claimKey: btcKey,
    }).webUrl;
    const btcPocket = new PocketSlipVault({
      slipUrl: btcSlipUrl,
      stateFilePath: null,
      publicClient: mockPublicClient,
      policy: { maxPerCallUsdMicro: 500_000n, maxDailyUsdMicro: 5_000_000n },
      transportOverrides: { directBroadcast, relayClient: offlineRelayClient },
    });
    await expect(
      btcPocket.payMerchantOrX402({
        recipient: allowedMerchant,
        amount: '500000',
        amountIsAtomic: true,
      }),
    ).rejects.toThrow(/exceeds maxPerCallUsdMicro/);

    // 3. USDC PocketSlip payHuman with strict allowedRecipients + 0 USDC operator wallet:
    // internal split hop to operatorAddress succeeds AND includes 100,000n ($0.10) paymaster headroom!
    const usdcSlipUrl = encodeSlipUrl({
      id: '303',
      amount: 5,
      asset: 'USDC',
      vault: 'v33',
      mode: 'open',
      claimKey: usdcKey,
    }).webUrl;
    const dummyMintedUrl = encodeSlipUrl({
      id: '999',
      amount: 0.25,
      asset: 'USDC',
      vault: 'v33',
      mode: 'open',
      claimKey: deriveKey('mcp-3r-human-out'),
    }).webUrl;

    const usdcPocket = new PocketSlipVault({
      slipUrl: usdcSlipUrl,
      stateFilePath: null,
      publicClient: mockPublicClient,
      policy: {
        maxPerCallUsdMicro: 500_000n,
        maxDailyUsdMicro: 5_000_000n,
        allowedRecipients: [allowedMerchant],
      },
      transportOverrides: { directBroadcast, relayClient: offlineRelayClient },
      customBatchExecutor: async () => ({
        prepared: {} as never,
        txHashes: [deriveKey('mcp-3r-mint-tx')],
        mintedSlips: [
          {
            index: 0,
            slipId: '999',
            txHash: deriveKey('mcp-3r-mint-tx'),
            blockNumber: 28_500_050,
            vault: 'v33',
            vaultAddress: CANONICAL_VAULT_V33_ADDRESS,
            creator,
            asset: 'USDC',
            grossAmountUnits: '250000',
            guaranteedNetClaimUnits: '248750',
            humanAmount: 0.25,
            mode: 'open',
            cancelLockedUntil: 0,
            claimSigner: allowedMerchant,
            payload: 'slip_999',
            url: dummyMintedUrl,
            sovereignUrl: dummyMintedUrl,
            telegramUrl: null,
          },
        ],
        csv: '',
        json: '[]',
      }),
    });

    const callsBeforeHuman = broadcastedCalls.length;
    const humanOut = await usdcPocket.payHuman({ amount: '0.25', asset: 'USDC' });
    expect(humanOut.outboundSlipUrl).toBe(dummyMintedUrl);
    // Boot Keep + SplitAndPay = 2 new calls; inspect the SplitAndPay paymentAmount (250,000 + 100,000 gas headroom grossed up)
    expect(broadcastedCalls.length).toBe(callsBeforeHuman + 2);
    const splitCall = broadcastedCalls[broadcastedCalls.length - 1]!;
    const decodedSplit = decodeFunctionData({
      abi: CRYPTO_SLIP_VAULT_V32_ABI,
      data: splitCall.data,
    });
    expect(decodedSplit.functionName).toBe('splitAndPayWithPermit');
    expect(decodedSplit.args[1]).toBe(grossUpForExactNet(250_000n + 100_000n));

    // 4. Uncast createPublicClient({ chain: base, ... }) compiles cleanly under TS6 strictness
    const liveBaseClient = createPublicClient({
      chain: base,
      transport: http('https://mainnet.base.org'),
    });
    const uncastVault = new PocketSlipVault({
      publicClient: liveBaseClient,
      stateFilePath: null,
    });
    expect(uncastVault.publicClient).toBe(liveBaseClient);
  });
});
