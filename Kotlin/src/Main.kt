class Admin(name: String = "admin", password: Int = 12345){
    class NewApp(name : String, database: String){
        init{
            println("name: $name")
            print("database: $database")
        }
    }
    class fileWrite(var name : String = "", var Text: Unit){
        init{
            File(name).writeText(Text)
        }
    }


    init{
        if (name == "admin" && password == 12345){
            println("successfuly completed 💯")
        }else{
            println("in correct username or password")
        }
}

}


fun main() {
    Admin.Open("ex.kt")
}