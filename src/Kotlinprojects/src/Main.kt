

import kotlin.collections.listOf
import java.util.UUID
import java.util.concurrent.ThreadLocalRandom

fun map(vararg maplist : Any){
	for (i in maplist){
	println("maps{$i}")
}
} 
fun Kt(query: Unit = print("Query")){

	println("$query")

	
}
fun List(vararg list: Any){
	for (l in list){
		println("data: {${l}}")
	}
}

class Student(var name: String, var id: Int){
	var lisence = ThreadLocalRandom.current().nextLong()
	fun applyliscense(lisenc : Any){
		if (lisenc == lisence){
			var l = ThreadLocalRandom.current().nextLong()
			println("lic: $l")
		}else{
			println("failed")
		}
	}

}

class  people(var name: String)

fun main(){
		var peo = Student("ojudsonleo", 1)
		println(peo.applyliscense(peo.lisence))
} 