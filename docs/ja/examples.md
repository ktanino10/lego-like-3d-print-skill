# 作例と、そこから分かること

[English](../en/examples.md) · [使い方](usage.md) · [権利と注意](notices.md)

作者が制作して公開した2つのプロジェクトを紹介します。
**外部ページへのリンクのみ**で、画像・写真・モデルはこの配布物へ転載していません。
公開データがあること、CGがあること、実物で組めたことは別の証拠です。

<a id="brick-display"></a>
## Copilot Brick Display

[Repository](https://github.com/ktanino10/copilot-brick-display) ·
[公開サイト](https://ktanino10.github.io/copilot-brick-display/) ·
[Bの対話3D組立ガイド](https://ktanino10.github.io/copilot-brick-display/assembly-guide/B.html) ·
[実物制作記録](https://ktanino10.github.io/copilot-brick-display/build-log.html)

A/B/Cのブロック風卓上オブジェ。FreeCADデータ、実メッシュのBlender CG・組立アニメ、
印刷・組立ガイドをつなぐ例です。このスキルの寸法・手順は主に
**B DESK CLASSIC / 5.0-legible-plaques**を参照します。

[固定commit](https://github.com/ktanino10/copilot-brick-display/tree/0967390547184b342adea0d7e8659dc8ac8f153b):
`0967390547184b342adea0d7e8659dc8ac8f153b`。
[完成CG](https://github.com/ktanino10/copilot-brick-display/blob/0967390547184b342adea0d7e8659dc8ac8f153b/site/media/B-hero.png)は
デジタル画像で、完成全体の実物写真ではありません。
[印刷→組立の対応図](https://github.com/ktanino10/copilot-brick-display/blob/0967390547184b342adea0d7e8659dc8ac8f153b/site/assembly-guide/media/B-first-base.png)
も元の公開ページで確認できます。

| デジタル設計の基準 | 実物の確認範囲 |
| --- | --- |
| B: 191.8×80.2×238.6 mm / 150部品 / 28工程 | 2026-09-23に作者が台座・前面の組立を報告 |
| 台座: 191.8×79.8 mm / 高さ48 mm / 5段 | 顔を含む全150個の完成は未確認 |
| 台座19＋顔126＋前面2＋keeper3 | 嵌合保持力・強度・耐久・転倒の測定合格は未確認 |
| 黒2.4＋白1.2の銘板、下段ink高さ10 mm | 写真ごとのSTL版・実slicer設定の完全照合は未確認 |

公開汎用文字版・A/C・新しい題材へ物理合格を広げません。
元repoに包括ライセンスはありません。[固定版の権利説明](https://github.com/ktanino10/copilot-brick-display/blob/0967390547184b342adea0d7e8659dc8ac8f153b/docs/licensing.md)
を確認し、画像やCADを自由に転載できるとは扱わないでください。

<a id="octoprints"></a>
## Octoprints brick-kit archive

[Repository](https://github.com/ktanino10/octoprints-brick-kit-downloads) ·
[日本語サイト](https://ktanino10.github.io/octoprints-brick-kit-downloads/ja/) ·
[English site](https://ktanino10.github.io/octoprints-brick-kit-downloads/en/) ·
[r3の保存リリース](https://github.com/ktanino10/octoprints-brick-kit-downloads/releases/tag/archive-2026-09-20-r3)

Mona / Copilot / Duckyをブロック化したデザインと、試作・改善の公開アーカイブです。
**参照版`r3-8mm-20260920`は8 mm共通ブロック**。
旧4 mm細密試作で小ささ・小ピン・穴詰まりが問題になった学びとは版を分けます。
r3の実物嵌合・保持・全体組立は未確認で、形状3MFは**NOT_SLICED**です。
Bとは別系統であり、部品数や実物結果を混ぜません。

**固定参照版と現在の進行状況:** 公開READMEにはr3後の個数倍率・支台なしの実験、
Copilot左右対称性の修正中という記録もあります。
r3だけが現在の全案である、全案が完成・実物合格した、と紹介するものではありません。
最新の対象版・保留事項はリンク先READMEで確認してください。

対象モデル派生物は**CC BY-NC 4.0**です。
[出典と権利区分](https://github.com/ktanino10/octoprints-brick-kit-downloads/blob/main/ATTRIBUTION.md)
を確認してください。このスキルのMITで非商用条件を上書きしません。

<a id="lessons"></a>
## 引き継ぐのは、作り方と確認の姿勢

共通部品を優先すること、実形状からCGを作ること、刷ったslotと組立位置をつなぐこと、
小試験から進めることを引き継ぎます。元のキャラクター・配色・ロゴ・個人宛文字の複製は既定にしません。
旧4 mmの失敗を8 mm Bの測定結果へ読み替えず、設計・報告・写真・実測を区別します。
