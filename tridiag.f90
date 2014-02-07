
      subroutine solve_tridiag(a,b,c,v,x,n) !from wikipedia
      implicit none
!      a - sub-diagonal (means it is the diagonal below the main diagonal)
!      b - the main diagonal
!      c - sup-diagonal (means it is the diagonal above the main diagonal)
!      v - right part
!      x - the answer
!      n - number of equations
 
        integer,intent(in) :: n
        real(8),dimension(n),intent(in) :: a,b,c,v
        real(8),dimension(n),intent(out) :: x
        real(8),dimension(n) :: bp,vp
        real(8) :: m
        integer i
 
! Make copies of the b and v variables so that they are unaltered by this subroutine
        bp(1) = b(1)
        vp(1) = v(1)
 
        !The first pass (setting coefficients):
firstpass: do i = 2,n
         m = a(i)/bp(i-1)
         bp(i) = b(i) - m*c(i-1)
         vp(i) = v(i) - m*vp(i-1)
        end do firstpass
 
         x(n) = vp(n)/bp(n)
        !The second pass (back-substition)
backsub:do i = n-1, 1, -1
          x(i) = (vp(i) - c(i)*x(i+1))/bp(i)
        end do backsub
 	

    	end subroutine solve_tridiag
