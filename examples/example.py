import easydbio

db = easydbio.DB({
  "database": "746ba518-b200-4cd8-8a8e-68fda649d45a",
  "token": "797e0f28-d84b-492c-91f5-8c72a20f5f81"
})

db.Put("key", "8")
print(db.Get("key"))
print(db.List())
# print(db.Get("key"))
# db.Delete("key")
# print(db.Get("key"))
# print(db.List())