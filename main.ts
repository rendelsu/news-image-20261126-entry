// news-image-20261126 entry (Node 22, standard library only): copies the
// committed entry.png next to this file to /output/entry.png. The image is
// rendered locally by render.py; the runtime never renders or uses the
// network, so the output bytes are deterministic.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   MAKEFUN_OUTPUT_DIR=out node main.ts

import { chmodSync, copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
const outFile = join(outDir, 'entry.png');
copyFileSync(new URL('./entry.png', import.meta.url), outFile);
chmodSync(outFile, 0o644);
