/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        var n1 = l1
        var n2 = l2

        val head = ListNode(0)
        var current = head
        var divideResult = plus(n1, n2)
        current.`val` = divideResult.remain
        if (n1?.next == null && n2?.next == null) {
            if (divideResult.divider > 0) current.next = ListNode(divideResult.divider)
            return head
        }

        n1 = n1?.next
        n2 = n2?.next
        divideResult = plus(n1, n2, divideResult.divider)
        while (n1?.next != null || n2?.next != null) {
            current.next = ListNode(0)
            current = current.next!!
            current.`val` = divideResult.remain

            n1 = n1?.next
            n2 = n2?.next
            divideResult = plus(n1, n2, divideResult.divider)
        }
        if (divideResult.divider != 0 || divideResult.remain != 0) {
            current.next = ListNode(divideResult.remain)
            current = current.next!!
            if (divideResult.divider > 0) current.next = ListNode(divideResult.divider)
        }
        return head
    }
}

data class DivideResult(val divider: Int, val remain: Int)

fun plus(node1: ListNode?, node2: ListNode?, more: Int = 0): DivideResult {
   var sum = (node1?.`val` ?: 0) + (node2?.`val` ?: 0) + more
   return DivideResult(sum / 10, sum % 10)
}


// end

class ListNode(var `val`: Int) {
    var next: ListNode? = null

    override fun toString(): String {
        return `val`.toString() + (if (next != null) " -> " + next.toString() else "")
    }
}

fun createNode(arr: List<Int>): ListNode {
    var first = ListNode(0)
    var node = first
    for (i in arr) {
        node.next = ListNode(i)
        node = node.next!!
    }
    return first.next!!
}

fun main(args: Array<String>) {
    // [7,0,8]
    println(Solution().addTwoNumbers(createNode(listOf<Int>(2, 4, 3)),
        createNode(listOf<Int>(5, 6, 4))).toString())
    // [7,9,0,1,3,3,4,2,7,2]
    println(Solution().addTwoNumbers(createNode(listOf<Int>(1,6,0,3,3,6,7,2,0,1)),
        createNode(listOf<Int>(6,3,0,8,9,6,6,9,6,1))).toString())
}