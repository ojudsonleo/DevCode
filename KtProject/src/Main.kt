fun dataStroager(){
    fun DataInt(value: Int){
        var DInt = listOf("$value")
    }
    fun DataString(value: String){
        var DString = listOf("$value")
    }
    fun DataBolean(value: Boolean){
        
        var DBolean = listOf("$value")
    }
    fun DataFloat(value: Float){
        var DFloat = listOf("$value")
    }
    fun DataLong(value: Long){
        var Dlong = listOf("$value")
    }
    fun DataShort(value: Short){
        var DShort = listOf("$value")
    }
}

fun main() {
    var d = dataStroager.DataInt(123)
}