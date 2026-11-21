import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { z } from 'zod';
import {
  redactSecretsFromToolOutput,
  type PaymentReceiptBundleV1,
  type ReceiptSettlementType,
} from '@cryptoslip/sdk';
import {
  PocketSlipVault,
  type PocketSlipVaultConfig,
} from './pocketSlip.js';

export const CRYPTOSLIP_MCP_TOOL_NAMES = [
  'cryptoslip_status',
  'cryptoslip_pay_human',
  'cryptoslip_batch_payout',
  'cryptoslip_pay_x402_or_merchant',
  'cryptoslip_verify_or_export_receipt',
  'cryptoslip_reclaim_unclaimed',
  'cryptoslip_withdraw_referrals',
] as const;

export interface CreateCryptoSlipMcpServerOptions {
  vault?: PocketSlipVault;
  vaultConfig?: PocketSlipVaultConfig;
}

function formatJsonResult(payload: unknown): {
  content: Array<{ type: 'text'; text: string }>;
} {
  return {
    content: [
      {
        type: 'text',
        text: JSON.stringify(payload, null, 2),
      },
    ],
  };
}

function formatErrorResult(err: unknown): {
  isError: true;
  content: Array<{ type: 'text'; text: string }>;
} {
  const rawMessage = err instanceof Error ? err.message : String(err);
  const safeMessage = redactSecretsFromToolOutput(rawMessage);
  const errorCode =
    typeof err === 'object' && err !== null && 'code' in err && typeof err.code === 'string'
      ? err.code
      : err instanceof Error
        ? err.name
        : 'ERROR';
  return {
    isError: true,
    content: [
      {
        type: 'text',
        text: JSON.stringify(
          {
            ok: false,
            errorCode,
            error: safeMessage,
          },
          null,
          2,
        ),
      },
    ],
  };
}

const assetEnum = z.enum(['USDC', 'cbBTC', 'BTC', 'ETH', 'NARA']);

/**
 * Creates a configured `McpServer` exposing all 7 `PocketSlip` non-custodial Base Mainnet (`8453`) tools.
 */
export function createCryptoSlipMcpServer(
  options: CreateCryptoSlipMcpServerOptions = {},
): {
  server: McpServer;
  pocketVault: PocketSlipVault;
} {
  const pocketVault = options.vault ?? new PocketSlipVault(options.vaultConfig);

  const server = new McpServer({
    name: '@cryptoslip/mcp',
    version: '1.0.0',
  });

  // 1. cryptoslip_status
  server.tool(
    'cryptoslip_status',
    'Returns the active PocketSlip balance, Base Mainnet v33 vault address, boot rotation status, and BoundedAgentPolicy limits with zero raw keys.',
    {},
    async () => {
      try {
        const status = await pocketVault.getStatus();
        return formatJsonResult(status);
      } catch (err) {
        return formatErrorResult(err);
      }
    },
  );

  // 2. cryptoslip_pay_human
  server.tool(
    'cryptoslip_pay_human',
    'Creates or splits a 1-tap #startapp=slip_... payout link (or 12-character scrypt claim code) for paying a human contributor over Telegram, X DM, or SMS.',
    {
      amount: z
        .string()
        .describe('Human decimal amount (e.g. "1.50") or atomic integer when amountIsAtomic is true'),
      amountIsAtomic: z.boolean().optional(),
      asset: assetEnum.optional(),
      noTakeBack: z
        .boolean()
        .optional()
        .describe('Set true for permanent No take-back finality (9_999_999_999); false allows 0%-fee reclaim if unclaimed'),
      mode: z.enum(['open', 'code']).optional(),
      grossUpForExitFee: z.boolean().optional(),
      note: z.string().max(120).optional(),
      recipientLabel: z.string().max(64).optional(),
    },
    async (args) => {
      try {
        const res = await pocketVault.payHuman(args);
        return formatJsonResult(res);
      } catch (err) {
        return formatErrorResult(err);
      }
    },
  );

  // 3. cryptoslip_batch_payout
  server.tool(
    'cryptoslip_batch_payout',
    'Executes a 1-tx Multicall3 batch payout (1..500 slips) on Base Mainnet with Builder Code bc_ea68lz8s and returns JSON or CSV # links.',
    {
      items: z
        .array(
          z.object({
            amount: z.string(),
            amountIsAtomic: z.boolean().optional(),
            asset: assetEnum.optional(),
            noTakeBack: z.boolean().optional(),
            grossUpForExitFee: z.boolean().optional(),
            mode: z.enum(['open', 'code']).optional(),
            note: z.string().max(120).optional(),
            recipientRef: z.string().max(64).optional(),
          }),
        )
        .min(1)
        .max(500),
      format: z.enum(['json', 'csv', 'both']).optional(),
    },
    async (args) => {
      try {
        const res = await pocketVault.batchPayout(args);
        return formatJsonResult(res);
      } catch (err) {
        return formatErrorResult(err);
      }
    },
  );

  // 4. cryptoslip_pay_x402_or_merchant
  server.tool(
    'cryptoslip_pay_x402_or_merchant',
    'Pays an HTTP 402 API endpoint or merchant wallet from the active PocketSlip via splitAndPay with BoundedAgentPolicy, SlipMutex, and $0.10 remainder guard.',
    {
      recipient: z
        .string()
        .describe('0x Base wallet address, #startapp=pos_<address>, or #startapp=pay_<address> URL'),
      amount: z.string().describe('Amount to pay (decimal string unless amountIsAtomic is true)'),
      amountIsAtomic: z.boolean().optional(),
      endpointUrl: z
        .string()
        .optional()
        .describe('Optional HTTPS endpoint URL validated against policy allowedDomains'),
      allowFullCashOnDust: z.boolean().optional(),
    },
    async (args) => {
      try {
        const res = await pocketVault.payMerchantOrX402(args);
        return formatJsonResult(res);
      } catch (err) {
        return formatErrorResult(err);
      }
    },
  );

  // 5. cryptoslip_verify_or_export_receipt
  server.tool(
    'cryptoslip_verify_or_export_receipt',
    'Verifies a PaymentReceiptBundleV1 on Base Mainnet or exports a signed JSON/CSV/HTML payment receipt.',
    {
      action: z.enum(['verify', 'export']),
      bundleJson: z
        .string()
        .optional()
        .describe('Serialized PaymentReceiptBundleV1 JSON when action is "verify"'),
      expectedRecipient: z.string().optional(),
      minNetAmountAtomic: z.string().optional(),
      slipId: z.string().optional(),
      txHash: z.string().optional(),
      blockNumber: z.number().int().nonnegative().optional(),
      blockTimestamp: z.number().int().nonnegative().optional(),
      settlementType: z
        .enum([
          'mint',
          'claim',
          'keep',
          'split_pay',
          'combine_pay',
          'swap_pay',
          'direct_transfer',
        ])
        .optional(),
      asset: assetEnum.optional(),
      grossAmount: z.string().optional(),
      feeAmount: z.string().optional(),
      netAmount: z.string().optional(),
      recipient: z.string().optional(),
      merchantLabel: z.string().optional(),
      orderId: z.string().optional(),
      signWithOperatorKey: z.boolean().optional(),
      includeCsv: z.boolean().optional(),
      includeHtml: z.boolean().optional(),
    },
    async (args) => {
      try {
        if (args.action === 'verify') {
          if (!args.bundleJson) {
            throw new Error('bundleJson is required when action is "verify".');
          }
          const bundle = JSON.parse(args.bundleJson) as PaymentReceiptBundleV1;
          const res = await pocketVault.verifyOrExportReceipt({
            action: 'verify',
            bundle,
            options: {
              ...(args.expectedRecipient ? { expectedRecipient: args.expectedRecipient } : {}),
              ...(args.minNetAmountAtomic
                ? { minNetAmount: BigInt(args.minNetAmountAtomic) }
                : {}),
            },
          });
          return formatJsonResult(res);
        }

        if (
          !args.slipId ||
          !args.txHash ||
          args.blockNumber === undefined ||
          args.blockTimestamp === undefined ||
          !args.settlementType ||
          !args.asset ||
          !args.grossAmount ||
          !args.netAmount ||
          !args.recipient
        ) {
          throw new Error(
            'slipId, txHash, blockNumber, blockTimestamp, settlementType, asset, grossAmount, netAmount, and recipient are required when action is "export".',
          );
        }

        const res = await pocketVault.verifyOrExportReceipt({
          action: 'export',
          receiptInput: {
            slipId: args.slipId,
            txHash: args.txHash,
            blockNumber: args.blockNumber,
            blockTimestamp: args.blockTimestamp,
            settlementType: args.settlementType as ReceiptSettlementType,
            asset: args.asset,
            grossAmount: args.grossAmount,
            ...(args.feeAmount ? { feeAmount: args.feeAmount } : {}),
            netAmount: args.netAmount,
            recipient: args.recipient,
            ...(args.merchantLabel ? { merchantLabel: args.merchantLabel } : {}),
            ...(args.orderId ? { orderId: args.orderId } : {}),
          },
          signWithOperatorKey: args.signWithOperatorKey,
          includeCsv: args.includeCsv,
          includeHtml: args.includeHtml,
        });
        return formatJsonResult(res);
      } catch (err) {
        return formatErrorResult(err);
      }
    },
  );

  // 6. cryptoslip_reclaim_unclaimed
  server.tool(
    'cryptoslip_reclaim_unclaimed',
    'Scans or executes a 0%-fee refundSlipDirect on Base Mainnet to recover unclaimed revocable (cancelLockedUntil == 0) DM slips.',
    {
      slipId: z.string().optional().describe('Specific slipId to reclaim; omit to scan recent slips'),
      scanOnly: z.boolean().optional().describe('When true, lists reclaimable slips without submitting a transaction'),
      minAgeSeconds: z.number().int().nonnegative().optional(),
    },
    async (args) => {
      try {
        const res = await pocketVault.reclaimUnclaimed(args);
        return formatJsonResult(res);
      } catch (err) {
        return formatErrorResult(err);
      }
    },
  );

  // 7. cryptoslip_withdraw_referrals
  server.tool(
    'cryptoslip_withdraw_referrals',
    'Withdraws accumulated 0.25% (50/50 share) lifetime referralCredits across USDC, cbBTC, ETH, and NARA on Base Mainnet.',
    {
      to: z.string().optional().describe('Optional safe destination Base wallet address'),
      assets: z.array(assetEnum).optional(),
    },
    async (args) => {
      try {
        const res = await pocketVault.withdrawReferrals(args);
        return formatJsonResult(res);
      } catch (err) {
        return formatErrorResult(err);
      }
    },
  );

  return { server, pocketVault };
}

/**
 * Starts the `@cryptoslip/mcp` server over stdio and triggers eager `V-01` `bootAndRotate()`
 * when `CRYPTOSLIP_URL` is configured so `.env` slip keys rotate in `<1s` on boot.
 */
export async function startCryptoSlipStdioServer(
  options: CreateCryptoSlipMcpServerOptions = {},
): Promise<{
  server: McpServer;
  pocketVault: PocketSlipVault;
  transport: StdioServerTransport;
}> {
  const { server, pocketVault } = createCryptoSlipMcpServer(options);

  if (options.vaultConfig?.slipUrl || process.env.CRYPTOSLIP_URL) {
    // Eager V-01 boot rotation; errors log safely to stderr without exposing raw secrets
    try {
      await pocketVault.bootAndRotate();
    } catch (err) {
      const msg = err instanceof Error ? err.message : String(err);
      process.stderr.write(
        `[@cryptoslip/mcp] Boot rotation warning: ${redactSecretsFromToolOutput(msg)}\n`,
      );
    }
  }

  const transport = new StdioServerTransport();
  await server.connect(transport);
  return { server, pocketVault, transport };
}
