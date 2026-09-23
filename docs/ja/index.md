# ブロックでつくる。設計から組立まで。

**個人の趣味・学習を目的とした非公式の制作支援スキルです。各社の公式提供・推奨や、互換性・造形結果の保証を示すものではありません。**

8 mmピッチのブロック風模型を、見た目だけでなく、実際に分けて刷り、組み立てる。
FreeCADの実CAD、印刷部品、BlenderのCG、部品表、組立ガイドを、同じデータでつなぐ
GitHub Copilot用のスキルです。

[導入を始める](install.md) · [依頼例を見る](usage.md) · [公開作例を見る](examples.md)

<a id="overview"></a>
## つくるための「手順」を配布します

| このスキルが支援すること | 大切にすること |
| --- | --- |
| FreeCADの実ソリッド・FCStd・STEP・STL | 開いた下面、筒・リブ、実際に分離する部品 |
| 色別の形状3MF・部品表・工程図 | 刷ったファイルと組立位置を追える対応表 |
| Blender完成CG・組立動画・対話3D | 実部品と同じメッシュ・配置・工程 |
| 合意した作品のGitHub Pages | 公開許可、出典、実配信、確認範囲 |

完成模型一式の生成器やCADアプリは含みません。AIがこの手順を読み、
利用者のプロジェクトで必要な設計・生成処理を行います。
スキルを読むだけ・公開3Dを見るだけならFreeCADやBlenderは不要です。

<a id="start"></a>
## まずは、小さな確認から

1. [スキルをコピー](install.md#skill-install)して新しいセッションを開始。
2. [FreeCAD・Blenderを準備](install.md#freecad)し、test-onlyの小箱で実行環境を確認。
3. [題材と保存先を伝える](usage.md#first-request)。既定は1作品1案。
4. 嵌合試験と代表部品から、台座・前面、本体へ。物理確認前に全数印刷へ進まない。

[スキル単体ZIP](https://ktanino10.github.io/lego-like-3d-print-skill/downloads/lego-like-3d-print.zip) ·
[SHA-256](https://ktanino10.github.io/lego-like-3d-print-skill/downloads/lego-like-3d-print.zip.sha256) ·
[GitHubの配布フォルダー](../../.github/skills/lego-like-3d-print/SKILL.md)

<a id="baseline"></a>
## 基準は8 mm。合格の証拠は別。

ピッチ8.0 mm、本体9.6 mm、プレート3.2 mm。スタッドは径4.8 mm・高さ1.8 mm、
本体全寸法差0.2 mm、メスの**半径方向**クリアランス+0.04 mm。
積層は9.6 mmで、完成STL全体の拡大縮小はしません。

参照Bは191.8×80.2×238.6 mm、150部品、28工程。
2026-09-23の実物報告は台座・前面までで、顔を含む全数や保持力・強度・転倒の測定合格は未確認です。
形状3MFは**NOT_SLICED**です。[作例の確認範囲](examples.md)を参照してください。

<a id="rights"></a>
## 趣旨とライセンス上の許可は違います

趣味・学習向けという趣旨を掲げていますが、本スキルの新規文書・スクリプトは
**MITで、商用利用も認めます**。非商用限定・個人利用限定という条件は追加しません。
外部作品・写真・ロゴ・商標・フォント・アプリの権利は別です。
[注意事項](notices.md) · [MIT全文](../../LICENSE)
