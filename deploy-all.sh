#!/bin/bash
set -e

TOKEN="${VERCEL_TOKEN}"
if [ -z "$TOKEN" ]; then
    echo "Notice: VERCEL_TOKEN environment variable not set. Using default Vercel CLI session."
fi
SITES=("aquafix" "autopro" "cleanpro" "dentacare" "glowup" "ironforge" "legalline" "sakartvelo-homes" "sweetest-house" "techfix")

echo "=== Deploying 10 Custom Demo Websites to Vercel Production ==="

for site in "${SITES[@]}"; do
    echo ""
    echo "▶ Deploying $site..."
    cd "$(dirname "$0")/$site"
    if [ -n "$TOKEN" ]; then
        npx vercel --prod --yes --token "$TOKEN"
    else
        npx vercel --prod --yes
    fi
    echo "✓ $site deployed"
done

echo ""
echo "All 10 sites deployed successfully!"
