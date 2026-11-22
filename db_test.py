from database import init_db, create_memo, get_all_memos, get_memo, update_memo, delete_memo

# テーブルを作成
init_db()
print("テーブルを作成しました")

# メモを追加
memo_id = create_memo("買い物リスト", "牛乳、卵、パン")
print(f"メモを作成しました（ID: {memo_id}）")

# もう1件追加
memo_id2 = create_memo("議事録", "次回は来週月曜")
print(f"メモを作成しました（ID: {memo_id2}）")

# 全メモを取得
memos = get_all_memos()
print("\\n--- 全メモ一覧 ---")
for memo in memos:
    print(f"  ID:{memo['id']} | {memo['title']} | {memo['body']}")

# 特定のメモを取得
memo = get_memo(memo_id)
print(f"\\n--- メモ詳細 (ID:{memo_id}) ---")
print(f"  タイトル: {memo['title']}")
print(f"  本文: {memo['body']}")

# メモを更新
update_memo(memo_id, "買い物リスト（更新）", "牛乳、卵、パン、バター")
memo = get_memo(memo_id)
print(f"\\n--- 更新後 ---")
print(f"  タイトル: {memo['title']}")
print(f"  本文: {memo['body']}")

# メモを削除
delete_memo(memo_id2)
print(f"\\nID:{memo_id2} のメモを削除しました")

# 削除後の一覧
memos = get_all_memos()
print("\\n--- 削除後の全メモ一覧 ---")
for memo in memos:
    print(f"  ID:{memo['id']} | {memo['title']} | {memo['body']}")