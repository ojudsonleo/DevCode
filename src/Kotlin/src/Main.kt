fun Query(Q: Unit){
    println(Q)
}

class Idata(vararg Data: Int){
    var Array : Any = listOf(Data)
}

fun main() {
    var ds = Idata(12)
    println(ds.Array))
}