subroutine array_test(a,n,b)

    integer, intent(in) :: n
    integer, dimension(n),intent(in) :: a
    integer, dimension(n), intent(out) :: b

    do i=1,n
        b(i) = a(1)
    enddo

end subroutine

