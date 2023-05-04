	.file	"qsort5.c"
	.text
	.comm	a,8000,32
	.comm	mutex,40,32
	.globl	active
	.data
	.align 4
	.type	active, @object
	.size	active, 4
active:
	.long	1
	.text
	.globl	run_quicksort
	.type	run_quicksort, @function
run_quicksort:
.LFB6:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$32, %rsp
	movq	%rdi, -24(%rbp)
	movq	-24(%rbp), %rax
	movq	%rax, -8(%rbp)
	movq	-8(%rbp), %rax
	movl	4(%rax), %ecx
	movq	-8(%rbp), %rax
	movl	(%rax), %eax
	movl	$1, %edx
	movl	%ecx, %esi
	movl	%eax, %edi
	call	quicksort
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE6:
	.size	run_quicksort, .-run_quicksort
	.globl	quicksort
	.type	quicksort, @function
quicksort:
.LFB7:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$64, %rsp
	movl	%edi, -52(%rbp)
	movl	%esi, -56(%rbp)
	movl	%edx, -60(%rbp)
	movq	%fs:40, %rax
	movq	%rax, -8(%rbp)
	xorl	%eax, %eax
	movl	-52(%rbp), %eax
	cmpl	-56(%rbp), %eax
	jge	.L3
	movl	-56(%rbp), %eax
	cltq
	leaq	0(,%rax,8), %rdx
	leaq	a(%rip), %rax
	movsd	(%rdx,%rax), %xmm0
	movsd	%xmm0, -32(%rbp)
	movl	-52(%rbp), %eax
	movl	%eax, -48(%rbp)
	movl	-56(%rbp), %eax
	movl	%eax, -44(%rbp)
	jmp	.L5
.L7:
	addl	$1, -48(%rbp)
.L6:
	movl	-48(%rbp), %eax
	cltq
	leaq	0(,%rax,8), %rdx
	leaq	a(%rip), %rax
	movsd	(%rdx,%rax), %xmm1
	movsd	-32(%rbp), %xmm0
	comisd	%xmm1, %xmm0
	ja	.L7
	jmp	.L8
.L9:
	subl	$1, -44(%rbp)
.L8:
	movl	-44(%rbp), %eax
	cltq
	leaq	0(,%rax,8), %rdx
	leaq	a(%rip), %rax
	movsd	(%rdx,%rax), %xmm0
	comisd	-32(%rbp), %xmm0
	ja	.L9
	movl	-48(%rbp), %eax
	cmpl	-44(%rbp), %eax
	jg	.L5
	movl	-48(%rbp), %eax
	cltq
	leaq	0(,%rax,8), %rdx
	leaq	a(%rip), %rax
	movsd	(%rdx,%rax), %xmm0
	movsd	%xmm0, -24(%rbp)
	movl	-44(%rbp), %eax
	cltq
	leaq	0(,%rax,8), %rdx
	leaq	a(%rip), %rax
	movsd	(%rdx,%rax), %xmm0
	movl	-48(%rbp), %eax
	cltq
	leaq	0(,%rax,8), %rdx
	leaq	a(%rip), %rax
	movsd	%xmm0, (%rdx,%rax)
	movl	-44(%rbp), %eax
	cltq
	leaq	0(,%rax,8), %rdx
	leaq	a(%rip), %rax
	movsd	-24(%rbp), %xmm0
	movsd	%xmm0, (%rdx,%rax)
	addl	$1, -48(%rbp)
	subl	$1, -44(%rbp)
.L5:
	movl	-48(%rbp), %eax
	cmpl	-44(%rbp), %eax
	jle	.L6
	cmpl	$0, -60(%rbp)
	je	.L11
	movl	-56(%rbp), %eax
	subl	-52(%rbp), %eax
	cmpl	$8191, %eax
	jg	.L12
	movl	$0, -60(%rbp)
	jmp	.L11
.L12:
	leaq	mutex(%rip), %rdi
	call	pthread_mutex_lock@PLT
	movl	active(%rip), %eax
	cmpl	$15, %eax
	jg	.L13
	movl	active(%rip), %eax
	addl	$1, %eax
	movl	%eax, active(%rip)
	leaq	mutex(%rip), %rdi
	call	pthread_mutex_unlock@PLT
	movl	-52(%rbp), %eax
	movl	%eax, -16(%rbp)
	movl	-44(%rbp), %eax
	movl	%eax, -12(%rbp)
	leaq	-16(%rbp), %rdx
	leaq	-40(%rbp), %rax
	movq	%rdx, %rcx
	leaq	run_quicksort(%rip), %rdx
	movl	$0, %esi
	movq	%rax, %rdi
	call	pthread_create@PLT
	movl	-56(%rbp), %ecx
	movl	-48(%rbp), %eax
	movl	$1, %edx
	movl	%ecx, %esi
	movl	%eax, %edi
	call	quicksort
	leaq	mutex(%rip), %rdi
	call	pthread_mutex_lock@PLT
	movl	active(%rip), %eax
	subl	$1, %eax
	movl	%eax, active(%rip)
	leaq	mutex(%rip), %rdi
	call	pthread_mutex_unlock@PLT
	movq	-40(%rbp), %rax
	movl	$0, %esi
	movq	%rax, %rdi
	call	pthread_join@PLT
	jmp	.L3
.L13:
	leaq	mutex(%rip), %rdi
	call	pthread_mutex_unlock@PLT
.L11:
	movl	-60(%rbp), %edx
	movl	-44(%rbp), %ecx
	movl	-52(%rbp), %eax
	movl	%ecx, %esi
	movl	%eax, %edi
	call	quicksort
	movl	-60(%rbp), %edx
	movl	-56(%rbp), %ecx
	movl	-48(%rbp), %eax
	movl	%ecx, %esi
	movl	%eax, %edi
	call	quicksort
.L3:
	movq	-8(%rbp), %rax
	xorq	%fs:40, %rax
	je	.L15
	call	__stack_chk_fail@PLT
.L15:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE7:
	.size	quicksort, .-quicksort
	.section	.rodata
.LC0:
	.string	"%f\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB8:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	$0, %esi
	leaq	mutex(%rip), %rdi
	call	pthread_mutex_init@PLT
	movl	$0, -4(%rbp)
	jmp	.L17
.L18:
	call	rand@PLT
	cvtsi2sdl	%eax, %xmm0
	movl	-4(%rbp), %eax
	cltq
	leaq	0(,%rax,8), %rdx
	leaq	a(%rip), %rax
	movsd	%xmm0, (%rdx,%rax)
	addl	$1, -4(%rbp)
.L17:
	cmpl	$999, -4(%rbp)
	jle	.L18
	movl	$1, %edx
	movl	$999, %esi
	movl	$0, %edi
	call	quicksort
	movl	$0, -4(%rbp)
	jmp	.L19
.L20:
	movl	-4(%rbp), %eax
	cltq
	leaq	0(,%rax,8), %rdx
	leaq	a(%rip), %rax
	movq	(%rdx,%rax), %rax
	movq	%rax, %xmm0
	leaq	.LC0(%rip), %rdi
	movl	$1, %eax
	call	printf@PLT
	addl	$1, -4(%rbp)
.L19:
	cmpl	$999, -4(%rbp)
	jle	.L20
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE8:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:
