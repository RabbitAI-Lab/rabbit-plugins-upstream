import { NextRequest, NextResponse } from "next/server";
import { db } from "@/db";
import { sql } from "drizzle-orm";
import {
  enforceSecurityMiddleware,
  wrapSecureResponse,
  secureErrorResponse,
  SECURITY_CONFIG,
} from "@/lib/security";

export const dynamic = "force-dynamic";

export async function GET(request: NextRequest) {
  // Security enforcement (using default rate limit for health check)
  const securityResult = await enforceSecurityMiddleware(request, "default");
  if (!securityResult.allowed) {
    return securityResult.response;
  }
  const { context } = securityResult;

  try {
    // Simple database health check
    await db.execute(sql`SELECT 1`);
    
    const response = NextResponse.json({ ok: true });
    return wrapSecureResponse(response, context, "default");
  } catch (error) {
    console.error("[HEALTH CHECK ERROR]", error);
    return wrapSecureResponse(
      secureErrorResponse(SECURITY_CONFIG.errors.generic, 500),
      context,
      "default"
    );
  }
}
