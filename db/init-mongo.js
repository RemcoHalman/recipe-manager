db.createUser({
  user: "Remco",
  pwd: "Remco123",
  roles: [
    {
      role: "readWrite",
      db: "recipe-manager-db",
    },
  ],
});
