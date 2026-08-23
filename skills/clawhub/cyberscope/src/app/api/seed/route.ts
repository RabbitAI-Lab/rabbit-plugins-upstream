import { NextRequest, NextResponse } from "next/server";
import { db } from "@/db";
import { categories, methods, resources } from "@/db/schema";
import { categoriesData, methodsData, resourcesData } from "@/lib/seed-data";
import {
  enforceSecurityMiddleware,
  wrapSecureResponse,
  secureErrorResponse,
  SECURITY_CONFIG,
} from "@/lib/security";

export const dynamic = "force-dynamic";

export async function POST(request: NextRequest) {
  // 1. Security enforcement - strict rate limiting for seed endpoint
  const securityResult = await enforceSecurityMiddleware(request, "seed");
  if (!securityResult.allowed) {
    return securityResult.response;
  }
  const { context } = securityResult;

  try {
    // 2. Check if already seeded (idempotent operation)
    const existing = await db.select({ id: categories.id }).from(categories).limit(1);
    if (existing.length > 0) {
      const response = NextResponse.json({ 
        message: "Database already seeded", 
        seeded: false 
      });
      return wrapSecureResponse(response, context, "seed");
    }

    // 3. Insert categories
    const insertedCategories = await db
      .insert(categories)
      .values(categoriesData)
      .returning({ id: categories.id, slug: categories.slug });

    // 4. Build slug->id map
    const catMap = new Map<string, number>();
    for (const cat of insertedCategories) {
      catMap.set(cat.slug, cat.id);
    }

    // 5. Insert methods
    const methodsToInsert = methodsData.map((m) => ({
      categoryId: catMap.get(m.categorySlug)!,
      methodNumber: m.methodNumber,
      title: m.title,
      description: m.description,
      keywords: m.keywords,
    }));

    const insertedMethods = await db
      .insert(methods)
      .values(methodsToInsert)
      .returning({ id: methods.id, methodNumber: methods.methodNumber });

    // 6. Build methodNumber->id map
    const methodMap = new Map<number, number>();
    for (const m of insertedMethods) {
      methodMap.set(m.methodNumber, m.id);
    }

    // 7. Insert resources
    const resourcesToInsert = resourcesData.map((r) => ({
      methodId: methodMap.get(r.methodNumber)!,
      title: r.title,
      url: r.url,
      source: r.source,
      resourceType: r.resourceType,
      description: r.description,
    }));

    await db.insert(resources).values(resourcesToInsert);

    // 8. Return success response
    const response = NextResponse.json({
      message: "Database seeded successfully",
      seeded: true,
      counts: {
        categories: insertedCategories.length,
        methods: insertedMethods.length,
        resources: resourcesToInsert.length,
      },
    });

    return wrapSecureResponse(response, context, "seed");
  } catch (error) {
    // Log error internally but don't expose details
    console.error("[SEED ERROR]", error);
    return wrapSecureResponse(
      secureErrorResponse(SECURITY_CONFIG.errors.generic, 500),
      context,
      "seed"
    );
  }
}
